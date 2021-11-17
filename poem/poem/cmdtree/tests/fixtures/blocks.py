import pytest
def fix(block):
    import textwrap
    return textwrap.dedent(block).strip()
class BlockNamespace: pass

SOL     = BlockNamespace()
PLANET  = BlockNamespace()
URANUS  = BlockNamespace()
EUROPA  = BlockNamespace()
JUPITER = BlockNamespace()

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

JUPITER.dlong = fix("""
    The planet JUPITER, also known as "The Red Giant",
    is the largest planet in the solar system.
    """)

   # """k"
   # The red giant
   # Jupiter is a planet with many moons.
#
#    It has a giant red spot.
#    """)

JUPITER.dnames = 'sol planet jupiter'
SOL.dnames = 'sol'

