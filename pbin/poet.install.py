#!/usr/bin/env python3
import textwrap
import sys
import os
import shutil
from pathlib import Path
from argparse import ArgumentParser as AP

parser=AP()
parser.add_argument( 'args', nargs='*')
parser.add_argument( '--clone'    , '-c',  action='store_true' )
parser.add_argument( '--install'  , '-i',  action='store_true' )

OOO = parser.parse_args()

RECLONE=OOO.clone
REINSTALL=OOO.install
FLAG  = Path(os.environ['POET_FLAG'])
BASE  = Path(os.environ['POET_BASE'])
INFO  = Path(os.environ['POET_INFO'])
BASE.exists() or BASE.mkdir()
INFO.exists() or INFO.mkdir()

NAME    = f'blessed.{OOO.args[0]}'
OPTIONS = ' '.join(OOO.args[1:])
SOURCE  = f'git@github.com:bryanhann/{NAME}'
REPO    = BASE/NAME
INSTALL = REPO/'install'
SEENFILE = INFO/NAME

def flag(name):
    path=FLAG/name
    if path.exists():
        return path.read_text().strip()
    return None

verbose = flag( 'poet.bless.verbose' )

def main():
    status()
    clone()
    install()

def status():
    if verbose == 'long':
        print(f"[poet.install.py]: {OOO.args}")
        print(textwrap.dedent(f"""\
        [poet.install.py]: {OOO.args}
            iscloned={REPO.exists()} reclone={OOO.clone}
            isinstalled={SEENFILE.exists()} reinstall={OOO.install}
            """).strip())

def note(msg):
    if verbose == 'long':
        print(f'    ({msg})')

def clone():
    if REPO.exists() and OOO.clone:
        note( 'clone: removing' )
        shutil.rmtree(REPO)
    if REPO.exists():
        note( 'clone: ignoring' )
        return
    note( 'clone: cloning' )
    cmd = f"git clone {SOURCE} {OPTIONS} {REPO}"
    cmd = cmd + " > /dev/null 2> /dev/null"
    os.system(cmd)

def install():
    if SEENFILE.exists() and OOO.install:
        note( 'install: removing' )
        os.remove(SEENFILE)
    if SEENFILE.exists():
        note( 'install: ignoring' )
        return
    note( 'install: installing' )
    SEENFILE.touch()
    os.system( INSTALL )

main()
