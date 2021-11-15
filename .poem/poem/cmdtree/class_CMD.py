#!/usr/bin/env python3

from pathlib import Path

def TF(*args):
    fix=lambda x : x and 'T' or 'F'
    return ''.join(list(map(fix,args)))

def lfilter(*a,**b):
    return list(filter(*a,**b))

def main4path(path):
    P1 = path/'__main__'
    P2 = Path(str(path)+'.__main__')
    for candidate in path, P1, P2:
        F = candidate.is_file()
        A = candidate.name == '__main__'
        B = candidate.suffix == '.__main__'
        if (F and (A or B)):
            return candidate

class Exc_CMD(Exception):
    pass

class CMD:
    def __repr__(self):
        return f'<CMD:{self.name}>'
    @property
    def dusage(self): return self.usage_block




    @property
    def usage_block(self):
        def padded(block):
            import textwrap
            return textwrap.indent(block,' '*4)
        if self.subcmd_block:
            return "\n".join(
                [ "USAGE:"       , padded(f"{self.dcallname} SUBCOMMAND")
                , "SUBCOMMANDS:" , padded(self.subcmd_block)
                , "DOCSTRING:"   , padded(self.long)
                ])
        else:
            return "\n".join(
                [ "USAGE:"     , padded( self.dcallname)
                , "DOCSTRING:" , padded(self.long)
                ])

    @property
    def subcmd_lines(self):
        cmds = self.subcmds
        width = lambda x : len(x.name)
        if cmds:
            mwidth = max(map(width,cmds))
        for cmd in cmds:
            yield f"{cmd.name.ljust(mwidth)} -- {cmd.short}"

    @property
    def subcmd_block(self):
        return "\n".join(list(self.subcmd_lines))

    @property
    def dsubcmd(self):
        return self.subcmd_block

    def __init__(self,path):
        isfile = path.is_file()
        isnode = path.name == '__main__'
        isleaf = path.suffix == '.__main__'
        isgood = isfile and (isnode or isleaf)
        if not isgood:
            raise Exc_CMD('Not a path')
        self._path = path

    @property
    def parents(self):
        def get_parents(self):
            xx = self.parent
            while xx: yield xx; xx = xx.parent
        return get_parents(self)

    @property
    def names(self):
        return [self.name] + [x.name for x in self.parents]

    @property
    def dnames(self):
        xx = self.names
        xx.reverse()
        return ' '.join(xx)
    @property
    def dcallname(self):
        return self.dnames
    def with_dunder(self,dunder):
        assert type(dunder)==type('')
        LD = TF(self.is_leaf,dunder)
        if LD == 'TT':  return self.path.with_suffix('.' + dunder)
        if LD == 'TF':  return self.path.with_suffix()
        if LD == 'FT':  return self.path.parent/dunder
        if LD == 'FF':  return self.path.parent
        raise AssertionError('NOT REACHABLE')

    @property
    def short(self):
        return self.dblock.split('\n')[0].strip() or "undocumented"
    @property
    def dshort(self): return self.short

    @property
    def long(self):
        lines = self.dblock.split('\n'); lines.pop(0)
        while lines and not lines[0].strip(): lines.pop(0)
        while lines and not lines[-1].strip(): lines.pop(-1)
        return '\n'.join(lines)
    @property
    def dlong(self): return self.long

    @property
    def dblock(self):
        try:
            return self.with_dunder('__doc__').read_text().strip()
        except FileNotFoundError:
            return ""#"None\nNone\n"

    @property
    def parent(self):
        path = self.is_leaf\
            and self.path.parent/'__main__'\
            or  self.path.parent.parent/'__main__'
        return path.is_file()\
            and CMD(path)\
            or None

    @property
    def is_leaf(self):
        return not self.path.name == '__main__'

    @property
    def path(self):
        return self._path

    @property
    def name(self):
        return self.is_leaf\
            and self.path.with_suffix('').name\
            or  self.path.parent.name

    @property
    def subcmds(self):
        return list(map(CMD,self._subcmd_paths()))

    def _subcmd_paths(self):
        keep = lambda x: x and not x==self._path
        if self.is_leaf:
            return []
        else:
            paths = self.path.parent.glob('*')
            return sorted(lfilter(keep,map(main4path,paths)))
