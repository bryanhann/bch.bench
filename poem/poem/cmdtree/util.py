#!/usr/bin/env python3


def padded(block):
    import textwrap
    return textwrap.indent(block,' '*4)

def TF(*args):
    fix=lambda x : x and 'T' or 'F'
    return ''.join(list(map(fix,args)))

def lfilter(*a,**b):
    return list(filter(*a,**b))

def reversed(aList):
    aa=aList.copy()
    aa.reverse()
    return aa

'''

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


def _isnode(p): return p.name == '__main__'
def _isleaf(p): return p.suffix == '.__main__'
def _isfile(p): return p.is_file()
def _isgood(p): return _isfile(p) and (_isleaf(p) or _isnode(p))

def with_dunder(path, dunder):
        assert type(dunder)==type('')
        LD = TF(_isleaf(path),dunder)
        if LD == 'TT':  return path.with_suffix('.' + dunder)
        if LD == 'TF':  return path.with_suffix()
        if LD == 'FT':  return path.parent/dunder
        if LD == 'FF':  return path.parent
        raise AssertionError('NOT REACHABLE')

def main4path(path):
    from pathlib import Path
    P1 = path/'__main__'
    P2 = Path(str(path)+'.__main__')
    for candidate in path, P1, P2:
        F = candidate.is_file()
        A = candidate.name == '__main__'
        B = candidate.suffix == '.__main__'
        if (F and (A or B)):
            return candidate

'''

