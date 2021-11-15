def test_dblock__europa  (C,B): assert C. europa  .dblock  == B. europa .dblock
def test_dblock__jupiter (C,B): assert C. jupiter .dblock  == B. jupiter .dblock
def test_dblock__uranyus (C,B): assert C. uranus  .dblock  == B. uranus .dblock
def test_dlong___europa  (C,B): assert C. europa  .dlong   == B. europa .dlong
def test_dshort__europa  (C,B): assert C. europa  .dshort  == B. europa .dshort
def test_dsubcmd_planet  (C,B): assert C. planet  .dsubcmd == B. planet .dsubcmd
def test_dsubcmd_io      (C,B): assert C. io      .dsubcmd == ""
def test_dcname__europa  (C,B): assert C.europa  .dnames ==  B. europa .dnames
def test_jupiter (C,B):
    assert C.jupiter .dnames \
       ==  B.jupiter .dnames
def test_europa  (C,B):
    assert C.europa  .dnames \
       ==  B.europa  .dnames

def test_sol(C,B):
    assert C.sol     .dnames \
       ==  B.sol     .dnames




