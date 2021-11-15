#!/usr/bin/env python3
import sys
import os
from pathlib import Path
from textwrap import dedent, indent
#BIN=Path(os.environ['POET_BIN'])

PAD='    '
def padprint(string):
    print(PAD + string)

def is_main_4path(p):
    if p.is_file()             : return False
    if p.name   == '__main__'  : return True
    if p.suffix == '.__main__' : return True
    if True                    : return False
def cmd4path(p):
    for xx in [p, (p/'__main__'), Path(str(p)+'.__main__')]:
        if not xx.is_file()         : continue
        if xx.name == "__main__"    : return xx
        if xx.suffix == ".__main__" : return xx
def shortdocstring(path):
    try: block = Path(str(path)+'.__short__').read_text()
    except FileNotFoundError: block = 'undocumented'
    return block.split('\n')[0]

class ABC_Cmd:
    def __init__(self,path):
        self._path = Path(path)
    @property
    def path(self): return self._path
    @property
    def name(self): return '/'.join(self.parts)
    @property
    def parts(self): raise Exception('\nPure Virtulail')
    @property
    def docfile(self): raise Exception('\nPure Virtulail')

    def subcmds(self): raise Exception('\nPure Virtulail')


    def docstring(self):
        try: return self.docfile.read_text()
        except FileNotFoundError: return 'None'

    def dump_usage(self):
        if self.subcmds():
            print( f'\nUSAGE:\n{PAD}{self.name} SUBCOMMAND' )
        else:
            print( f'\nUSAGE:\n{PAD}{self.name}' )

    def dump_subcmds(self):
        if not self.subcmds():
            return
        print('\nSUBCOMMANDS:')
        acc = {}
        for cmd in self.subcmds():
            acc[ cmd.name ] = shortdocstring(cmd)
        L = max(len(key) for key in acc.keys())
        for key,val in acc.items():
            print( f"{PAD}{key.ljust(L)}  -- {val}" )


    def dump_docstring(self):
        print('\nDOCSTRING:')
        print(indent(self.docstring(),PAD))

    def dump(self):
        self.dump_usage()
        self.dump_subcmds()
        self.dump_docstring()

class FileCmd(ABC_Cmd):
    def __init__(self,path):
        ABC_Cmd.__init__(self,path)
        self._parent = DirCmd(self.path.parent)
        assert self.path.is_file()

    @property
    def docfile(self):
        return Path(str(self.path)+'.__doc__')

    @property
    def parts(self):
        return self._parent.parts + [self.path.name]

    def subcmds(self):
        return []




class DirCmd(ABC_Cmd):
    def __init__(self,path):
        ABC_Cmd.__init__(self,path)
        assert self.path.is_file()
        assert (
            self.path.name=='__main__'
            or self.path.suffix=='.__main__'
        )
    @property
    def cmdname(self):
        if self.path.name=='__main__':
            return self.path.parent.name
        else:
            # remove suffix '.__main__'
            return '.'.join(self.path.name.split('.')[:-1])
    @property
    def docfile(self): return self.path/'__doc__'


    @property
    def parts(self):
        path = self.path
        acc = []
        while cmd4path(path):
            acc.insert(0,path.name)
            path = path.parent
        return acc

    def subcmds(self):
        if not self._path.name == '__main__':
            return []
        aa = self.path.parent.glob('*')
        aa = map(cmd4path, aa)
        aa = filter(None,aa)
        aa = [ xx for xx in aa if not xx==self._path ]
        aa = sorted(aa)
        return aa
'''

def docstring4path(path):
        docpath = Path(str(path)+'.__doc__')
        if docpath.is_file():
            return docpath.read_text()
        else:
            return 'None'
def usage_4dir():
    path=Path(sys.argv[1])
    assert path.is_dir()
    assert str(path).startswith(str(BIN))
    rpath = path.relative_to(BIN)
    parts = (str(rpath).split("/"))
    if parts == ['.']: parts = []
    for xx in parts: assert xx.endswith('.d')
    parts = [ xx[:-2] for xx in parts ]
    usage0(path,parts,[])

def usage_4file():
    path=Path(sys.argv[1])
    assert str(path).startswith(str(BIN))
    rpath = path.relative_to(BIN)
    parts = (str(rpath).split("/"))
    print(path)
def main():
    def append(path,name): return path/f"{name}.d"
    args = ['poet'] + sys.argv[1:]
    path = Path(os.environ['POET_BIN'])
    parts = []
    while args and append(path,args[0]).is_dir():
        path=append(path,args[0])
        parts.append(args.pop(0))
    if args and (path/args[0]).is_file():
        parts.append(args.pop(0))
        prefix = ' '.join(parts)
        print( f"Command [{prefix}]: stub help.")
    else:
        usage0(path, parts,args)

def cmdDict_4path(path):
    def is_poet_executable(path):
        if '.' in path.name:
            return False
        if path.name.startswith('__'):
            return False
        return True



    acc = dict()
    for xx in path.glob('*'):
        if is_poet_executable(xx):
            acc[ xx.name ] = docstring4path(xx).split('\n')[0]
    return acc

def usage0(path, parts, args):
    # DIR
    PAD='    '
    def longhelp_4path(path):
        doc = path/'__doc__'
        if doc.is_file():
            block=doc.read_text()
            block=indent(block, '    ')
        else:
            block="    None."
        print( "DOCSTRING:\n" + block)
    def usage_4cmdDict_4prefix(cmdDict,prefix):
        L = max(len(item) for item in cmdDict)
        for name,doc in cmdDict.items():
            print( f"{PAD}{name.ljust(L)}   {doc}" )
    prefix = ' '.join(parts)
    usage0=f"USAGE:\n{PAD}{prefix}"
    usage1=f"USAGE:\n{PAD}{prefix} COMMAND\nCOMMANDS:"
    cmdDict=cmdDict_4path(path)
    if cmdDict:
        print(usage1)
        usage_4cmdDict_4prefix(cmdDict,prefix)
    else:
        print( usage0 )
    longhelp_4path(path)

if __name__ == '__main__':
    main()
'''

