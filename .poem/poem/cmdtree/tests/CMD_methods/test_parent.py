def test_europa (C): assert C.europa .parent.name=='jupiter'
def test_jupiter(C): assert C.jupiter.parent.name=='planet'
def test_planet (C): assert C.planet .parent.name=='sol'
def test_sol    (C): assert C.sol    .parent==None

