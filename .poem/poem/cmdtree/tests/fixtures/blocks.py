import pytest
def fix(block):
    import textwrap
    return textwrap.dedent(block).strip()
class Namespace: pass

SOL     = Namespace()
PLANET  = Namespace()
URANUS  = Namespace()
EUROPA  = Namespace()
JUPITER = Namespace()

PLANET.dsubcmd = fix(
    """
    jupiter -- The red giant
    uranus  -- undocumented
    venus   -- The morning star
    """)

URANUS.dblock = fix(
    """
    """)

EUROPA.dblock = fix(
    """
    Avoid this moon!

    This moon is not for us.


    “All these worlds are yours. Except Europa.
    Attempt no landing there.”
        -- Arthur C. Clarke, _2010: Odyssey Two_
    """)

EUROPA.dlong = fix(
    """
    This moon is not for us.


    “All these worlds are yours. Except Europa.
    Attempt no landing there.”
        -- Arthur C. Clarke, _2010: Odyssey Two_
    """)

EUROPA.dshort = fix(
    """
    Avoid this moon!
    """)
EUROPA.dnames = 'sol planet jupiter europa'

JUPITER.dblock = fix(
    """
    The red giant
    Jupiter is a planet with many moons.

    It has a giant red spot.
    """)
JUPITER.dnames = 'sol planet jupiter'
SOL.dnames = 'sol'

