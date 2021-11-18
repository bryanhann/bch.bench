#!/usr/bin/env python3
import poem.cmdtree.class_CMD as _CC_
import poem.cmdtree.util as UU
from pathlib import Path
def _isnode(p): return p.is_file() and p.name == '__main__'
def _isleaf(p): return p.is_file() and p.suffix == '.__main__'
def _ismain(p): return _isnode(p) or _isleaf(p)
#def _isbase(p): return _ismain(p/'__main__') or _
def swap4main4dunder(main, dunder):
        assert type(dunder)==type('')
#        assert _ismain(main)
        if _isleaf(main):
            if dunder: return main.with_suffix( '.' + dunder )
            else:      return main.with_suffix()
        if _isnode(main):
            if dunder: return main.parent/dunder
            else:      return main.parent
        return None
        raise Exception('unreachable')

def main4path(path):
    from pathlib import Path
    P0 = path
    P1 = path/'__main__'
    P2 = Path(str(path)+'.__main__')
    for candidate in P0, P1, P2:
        F = candidate.is_file()
        A = candidate.name == '__main__'
        B = candidate.suffix == '.__main__'
        if (F and (A or B)):
            return candidate

def name4main(main):
    if _isleaf(main):
        return main.with_suffix('').name
    else:
        return main.parent.name

def cmd4main(main):
    if _ismain(main):
        return _CC_.CMD(main)

def _import(path):
    import importlib.util
    class MockModule:
        @property
        def SHORT(self): return 'undocumented'
        def LONG(self): return "None."
    if not (path and path.is_file()):
        return MockModule()
    spec = importlib.util.spec_from_file_location("anon", path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo

def base4main(main):
    assert _ismain(main)
    if _isleaf(main):
        return main.with_suffix('')
    else:
        return main.parent

def mainX_4base(base):
    d = base.is_dir()
    if d: mainX = base/'__main__'
    else: mainX = Path(str(base) + '__main__')
    mainX = _ismain(mainX) and mainX or None
    return mainX

def mainX_4path(path):
    if _ismain(path):
        return path
    else:
        return mainX_4base(path)

def pmain4main(main):
    pbase = pbase4main(main)
    pmain = pbase/'__main__'
    return pmain
def pcmd4main(main):
    pmain = pmain4main(main)
    return cmd4main(pmain)

def initfile4main(main):
    return swap4main4dunder(main, '__init__.py' )
def initmod4main(main):
    return _import( initfile4main(main) )

def pbase4main(main):
    return base4main(main).parent
