#!/usr/bin/env python3

import sys
import textwrap
from pathlib import Path

NL='\n'
MAGIC=" # 1636129536.480696"

def cleanblock_4_dotpath(dotpath):
    lines = dotpath.read_text().split(NL)
    lines = [ x for x in lines if not x.endswith(MAGIC) ]
    while lines and not lines[-1]:
        lines.pop(-1)
    return NL.join(lines) + NL

def make_extra(block):
    block = textwrap.dedent(block)
    aa = [ x for x in block.split(NL) if x.strip() ]
    LEN = max(len(x) for x in aa)
    bb = [ x.ljust(LEN) + MAGIC for x in aa]
    return NL.join(bb) + NL

def install_to_dotname(dotname):
    dotfile = Path.home()/dotname
    if dotfile.is_file():
        POET = Path(__file__).absolute().parent
        prefix  = f"poet[{dotname}]:"
        INSITU = Path(__file__).absolute().parent/'.insitu'
        HASH = '###'
        CLEAN = cleanblock_4_dotpath(dotfile)
        EXTRA = make_extra(f"""
            {HASH} BEGIN poet activation
                xx={INSITU}
                [ -d $xx ] || echo "{prefix} cannot activate {POET}"
                [ -d $xx ] && pushd $xx > /dev/null
                [ -d $xx ] && . ./activate.sh {dotname}
                [ -d $xx ] && popd > /dev/null
                xx=
            #{HASH} END poet activation
            """)
        if 'yes' in sys.argv:
            print(f"installed to {dotname}")
            dotfile.write_text(CLEAN + EXTRA)
        else:
            print(f"uninstalled from {dotname}")
            dotfile.write_text(CLEAN)


def main():
    THIS = Path(__file__)
    args=sys.argv[1:]
    args==['yes'] or args==['no'] or exit( print(textwrap.dedent(f"""
            USAGE:
                {THIS} yes   -- install poet to dotfiles
                {THIS} no    -- uninstall poet from dotfiles
            """)))
    install_to_dotname( '.profile' )
    install_to_dotname( '.bashrc' )

if __name__ == '__main__':
    main()
