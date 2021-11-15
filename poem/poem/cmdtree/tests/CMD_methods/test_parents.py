path4cmd = lambda cmd:cmd.path
lmap = lambda *x,**y : list(map(*x,**y))
def test_europa(C,Q):
    cmds = C.europa.parents
    paths = lmap(path4cmd,cmds)
    assert paths == [ Q.jupiter, Q.planet, Q.sol ]

