#!/usr/bin/env python3

import os
import sys
from pathlib import Path

SCRIPT=Path(__file__).absolute()

EPILOG=f"""
    This output should be sourced to activate your
    poet installation. If you are reading this you
    probably invoked:

        {SCRIPT}

    instead of:

        eval $({SCRIPT})
"""


class Exporter:
    """Output a script for sourcing.
    """
    def __init__(self,fd):
        """
        .fd is the file descriptor to use for output
        .store will accumulate the (k,v) pairs.
        """
        self.__dict__[ 'fd' ] = fd
        self.__dict__[ 'store' ] =  []

    def __setattr__(self, attrname, attrval):
        """ X.A=B will set environment var A to B
        """
        self.store.append( (attrname,str(attrval)))
    def write(self):
        """Write out the script to evaluate
        """
        for k,v in self.store:
            self.fd.write(f"export {k}={v}\n")
            self.fd.flush()
    def comment(self,block):
        """Add a block of commented text to the output
        """
        lines=block.split('\n')
        for line in lines:
            self.fd.write(f"# {line}\n")
        self.fd.flush()
    def unset(self,prefix):
        """Remove variables starting with prefix from the environment
        """
        for key in os.environ.keys():
            if key==prefix or key.startswith(prefix+'_'):
                setattr(self,key, '')
    def unpath(self,target):
        target=str(target)
        path=os.environ['PATH']
        parts=path.split(':')
        parts=[xx for xx in parts if not xx == target]
        path=':'.join(parts)
        return path

def main():
    exp=Exporter(sys.stdout)
    exp.unset( 'POET' )

    ROOT  = Path(__file__).absolute().parent.parent
    BIN   = ROOT/'.bin'

    if '-r' in sys.argv:
        exp.PATH = f"{exp.unpath(BIN)}"
    else:
        exp.PATH = f"{BIN}:{exp.unpath(BIN)}"
        exp.POET = ROOT
        exp.POET_BIN  = BIN
        exp.POET_USER = ROOT/'.user'
        exp.POET_POEM = ROOT/'.poem'
        exp.POET_VEND = ROOT/'.vend'

    exp.write()
    exp.comment(EPILOG)

if __name__=='__main__':
    main()
