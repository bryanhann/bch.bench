comp = lambda f2, f1 : lambda *x, **y : f2(f1(*x,**y))
lmap = comp(list,map)
lfilter = comp(list,filter)
