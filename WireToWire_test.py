#=========================================================================
# WireToWire_test
#=========================================================================

from pymtl      import *
from pclib.test import run_test_vector_sim
from WireToWire import WireToWire

def test_basic( dump_vcd ):
  run_test_vector_sim( WireToWire(), [
    ('in_   out*'),
    [ 0b00, '?'],
    [ 0b10,  0b10 ],
    [ 0b01,  0b10 ],
    [ 0b11,  0b11 ],
    [ 0b11,  0b11 ],
    [ 0b11,  0b11 ],
  ], dump_vcd )

