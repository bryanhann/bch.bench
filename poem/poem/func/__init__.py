#!/usr/bin/env python3

__comp = lambda f2, f1 : lambda *x, **y : f2(f1(*x,**y))
lmap = __comp(list,map)
lfilter = __comp(list,filter)
