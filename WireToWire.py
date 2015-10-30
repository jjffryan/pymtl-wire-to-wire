#=========================================================================
# WireToWire
#=========================================================================
# Simple test case for potential wire to wire connectivity bug.

from pymtl     import *
from pclib.rtl import Reg

class WireToWire( Model ):

  # Constructor

  def __init__( s ):

    s.in_ = InPort  ( 1 )
    s.out = OutPort ( 1 )

    s.wire1 = Wire( 1 )
    s.register = m = Reg( dtype = 1 )
    s.connect_pairs(
      m.in_, s.in_,
      m.out, s.wire1,
    )
    s.wire2 = Wire( 1 )
    s.connect( s.wire2, s.wire1 )

  # Line tracing

  def line_trace( s ):
    return "{} ({}) {}".format( s.in_, s.register.out, s.out )

