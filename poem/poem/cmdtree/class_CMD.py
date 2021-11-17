#!/usr/bin/env python3

from pathlib import Path

import poem.cmdtree.util    as UU__
import poem.cmdtree.cmdtool as TT__

lfilter = lambda *a,**b : list(filter(*a,**b))
lmap    = lambda *a,**b : list(map(*a,**b))

class Usage:
    @property
    def subcmds(self): return lmap(CMD,self._subcmd_paths())
    @property
    def dnames(self): return ' '.join(UU__.reversed(self.names))
    @property
    def dshort(self): return self.initmod.SHORT.strip()
    @property
    def dlong(self): return self.initmod.LONG.strip()

    @property
    def dsubcmd(self):
        names  = [cmd.name for cmd in self.subcmds]
        shorts = [cmd.dshort for cmd in self.subcmds]
        width  = names and max(map(len,names)) or 0
        names  = [ name.ljust(width) for name in names ]
        lines  = [ f"{n} -- {s}" for n,s in zip(names,shorts) ]
        return '\n'.join(lines)

    @property
    def dusage(self):
        DOCSTRING = [ "DOCSTRING"     , UU__.padded(self.dlong)  ]
        if self.dblock:
            USAGE       = [ "USAGE:"        , UU__.padded(self.dnames + ' COMMAND') ]
            SUBCOMMANDS = [ "SUBCOMMANDS:"  , UU__.padded(self.dblock) ]
        else:
            USAGE       = [ "USAGE:"        , UU__.padded(self.dnames) ]
            SUBCOMMANDS = []
        return '\n'.join(USAGE + SUBCOMMANDS + DOCSTRING)

    def _subcmd_paths(self):
        mainX4p = TT__.mainX_4path
        good = lambda mainX : mainX and not mainX == self.main
        paths = self.node and self.main.parent.glob('*') or []
        return sorted(lfilter(good,lmap(mainX4p,paths)))

class Exc_CMD(Exception):
    pass

class CMD(Usage):
    def __init__(self,main):
        assert TT__._ismain(main)
        self._main = main
        self._init = TT__.initmod4main(self.main)
    @property
    def parents(self):
        xx = self.parent
        while xx: yield xx; xx = xx.parent
    def __repr__(self): return f'<CMD:{self.name}>'
    @property
    def initmod(self): return self._init
    @property
    def superlist(self): return [self] + list( self.parents )
    @property
    def names(self): return [ x.name for x in self.superlist ]
    @property
    def parent(self): return TT__.pcmd4main(self.main)
    @property
    def leaf(self): return TT__._isleaf(self.main)
    @property
    def node(self): return not self.leaf
    @property
    def main(self): return self._main
    @property
    def name(self): return TT__.name4main(self.main)

