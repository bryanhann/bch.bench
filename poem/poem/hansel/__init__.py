#!/usr/bin/env python3

from pathlib import Path

import psutil

from poem.func import lmap, lfilter

def crumb4path(path):
    return path/'.bch'

def ishansel(path):
    return crumb4path(path).exists()

def roots():
    aa = psutil.disk_partitions(all=True)
    aa = [ xx.mountpoint for xx in aa ]
    aa = lmap(Path,aa) + [ Path.home() ]
    return lfilter(ishansel,aa)

def walkroot(root):
    if ishansel(root):
        yield root
        for path in root.glob('*'):
            yield from walkroot(path)

def walkall():
    for root in roots():
        yield from walkroot(root)

def showall():
    for hansel in walkall():
        print(hansel)

