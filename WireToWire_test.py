#=========================================================================
# WireToWire_test
#=========================================================================

from pymtl      import *
from pclib.test import run_test_vector_sim
from WireToWire import WireToWire

def test_basic( dump_vcd ):
  run_test_vector_sim( WireToWire(), [
    ('in_   out*'),
    [ 0, '?'],
    [ 1,  0 ],
    [ 0,  1 ],
    [ 1,  0 ],
    [ 1,  1 ],
    [ 1,  1 ],
  ], dump_vcd )

