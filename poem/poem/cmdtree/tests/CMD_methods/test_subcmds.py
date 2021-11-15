def test_planet(C,Q): assert C.planet ._subcmd_paths() == [Q.jupiter, Q.uranus, Q.venus]
def test_europa(C):   assert C.europa ._subcmd_paths() == []
def test_venus(C):    assert C.venus  ._subcmd_paths() == []
