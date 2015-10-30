#=========================================================================
# WireToWire
#=========================================================================
# Simple test case for potential wire to wire connectivity bug.

from pymtl     import *
from pclib.rtl import Reg

class WireToWire( Model ):

  # Constructor

  def __init__( s ):

    s.in_ = InPort  ( 2 )
    s.out = OutPort ( 2 )

    s.wire1 = Wire( 2 )
    s.register = m = Reg( dtype = 2 )
    s.connect_pairs(
      m.in_, s.in_,
      m.out, s.wire1,
    )
    s.wire2 = Wire( 2 )
    s.connect( s.wire2[0], s.wire1[0] )
    s.connect( s.wire2[1], 0b1 )
    s.connect( s.out,   s.wire2 )

  # Line tracing

  def line_trace( s ):
    return "{} ({}) {}".format( s.in_, s.register.out, s.out )

