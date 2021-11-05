#!/usr/bin/env python3

import os
import sys
from pathlib import Path

def unpath(target):
    target=str(target)
    path=os.environ['PATH']
    parts=path.split(':')
    parts=[xx for xx in parts if not xx == target]
    path=':'.join(parts)
    return path

class Exporter:
    def __init__(self,fd):
        self.__dict__[ 'store' ] =  []
        self.__dict__[ 'fd' ] = fd
    def __setattr__(self, attrname, attrval):
        self.store.append( (attrname,str(attrval)))
    def write(self):
        for k,v in self.store:
            self.fd.write(f"export {k}={v}\n")
            self.fd.flush()

def main():
    exp=Exporter(sys.stdout)
    POET_ROOT=Path(__file__).absolute().parent
    POET_BIN=POET_ROOT/'bin'
    if '-r' in sys.argv:
         exp.POET_ROOT  = ""
         exp.POET_BIN   = ""
         exp.PATH       = f"{unpath(POET_BIN)}"
    else:
         exp.POET_ROOT  = POET_ROOT
         exp.POET_BIN   = POET_BIN
         exp.PATH       = f"{POET_BIN}:{unpath(POET_BIN)}"
    exp.write()

if __name__=='__main__':
    main()
