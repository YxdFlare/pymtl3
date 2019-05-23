#=========================================================================
# BehavioralRTLIRFreeVar_test.py
#=========================================================================
# Author : Peitian Pan
# Date   : May 20, 2019
"""Test the free variable generation of behavioral RTLIR passes."""

from __future__ import absolute_import, division, print_function

import pytest

from pymtl import *
from pymtl.passes.rtlir.behavioral import (
    BehavioralRTLIRGenPass,
    BehavioralRTLIRTypeCheckPass,
)
from pymtl.passes.rtlir.behavioral.BehavioralRTLIR import *
from pymtl.passes.rtlir.errors import PyMTLTypeError
from pymtl.passes.rtlir.test_utility import do_test, expected_failure

# from test_module import pymtl_Bits_global_freevar


def local_do_test( m ):
  """Check if generated behavioral RTLIR is the same as reference."""
  m.apply( BehavioralRTLIRGenPass() )
  m.apply( BehavioralRTLIRTypeCheckPass() )
  ref = m._rtlir_freevar_ref
  ns = m._pass_behavioral_rtlir_type_check

  for fvar_name in ref.keys():
    assert fvar_name in ns.rtlir_freevars
    assert ns.rtlir_freevars[fvar_name] == ref[ fvar_name ]

def test_pymtl_Bits_closure_construct( do_test ):
  class A( Component ):
    def construct( s ):
      foo = Bits32( 42 )
      s.fvar_ref = foo
      s.out = OutPort( Bits32 )
      @s.update
      def upblk():
        s.out = foo
  a = A()
  a.elaborate()
  a._rtlir_freevar_ref = { 'foo' : a.fvar_ref }
  do_test( a )

def test_pymtl_Bits_closure_module( do_test ):
  foo = Bits32( 42 )
  class A( Component ):
    def construct( s ):
      s.out = OutPort( Bits32 )
      @s.update
      def upblk():
        s.out = foo
  a = A()
  a.elaborate()
  a._rtlir_freevar_ref = { 'foo' : foo }
  do_test( a )

pymtl_Bits_global_freevar = Bits32( 42 )

def test_pymtl_Bits_global( do_test ):
  class A( Component ):
    def construct( s ):
      s.out = OutPort( Bits32 )
      @s.update
      def upblk():
        s.out = pymtl_Bits_global_freevar
  a = A()
  a.elaborate()
  a._rtlir_freevar_ref = \
    { 'pymtl_Bits_global_freevar' : pymtl_Bits_global_freevar }
  do_test( a )

def test_pymtl_struct_closure( do_test ):
  class B( object ):
    def __init__( s, foo=42 ):
      s.foo = Bits32(foo)
  class A( Component ):
    def construct( s ):
      foo = InPort( B )
      s._foo = foo
      s.out = OutPort( Bits32 )
      @s.update
      def upblk():
        s.out = foo.foo
  a = A()
  a.elaborate()
  a._rtlir_freevar_ref = { 'foo' : a._foo }
  do_test( a )
