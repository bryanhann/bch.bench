#!
import pytest
from pathlib import Path
import poem.cmdtree.class_CMD as _CMD
import fixtures.blocks as _B

FIXTURES = Path(__file__).absolute().parent/'fixtures'

class Namespace():
    pass

@pytest.fixture
def ROOT():
    return FIXTURES/'root'

@pytest.fixture
def B():
    xx=Namespace()
    xx.europa = _B.EUROPA
    xx.jupiter = _B.JUPITER
    xx.planet = _B.PLANET
    xx.uranus = _B.URANUS
    xx.sol    = _B.SOL
    return xx

@pytest.fixture
def Q(ROOT):
    xx=Namespace()
    xx.sol      = ROOT/'sol/__main__'
    xx.planet   = ROOT/'sol/planet/__main__'
    xx.venus    = ROOT/'sol/planet/venus.__main__'
    xx.jupiter  = ROOT/'sol/planet/jupiter/__main__'
    xx.ganymede = ROOT/'sol/planet/jupiter/ganymede.__main__'
    xx.europa   = ROOT/'sol/planet/jupiter/europa.__main__'
    xx.io       = ROOT/'sol/planet/jupiter/io.__main__'
    xx.uranus   = ROOT/'sol/planet/uranus.__main__'
    return xx

@pytest.fixture
def C(Q):
    xx=Namespace()
    for (k,v) in Q.__dict__.items():
        try:
            setattr(xx,k,_CMD.CMD(v))
        except _CMD.Exc_CMD:
            setattr(xx,k,None)
    return xx
