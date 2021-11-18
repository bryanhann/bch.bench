#!/usr/bin/env python3

import textwrap

import poem.hansel

def doc(block):
    print( textwrap.dedent(block).strip() )

def hansel_usage():
    doc( """
         USAGE:
             hansel-walkall -- send all hansel paths to stdout
             hansel         -- this help
         """)
def hansel_walkall():
    for path in poem.hansel.walkall():
        print(path)
