#=========================================================================
# VBehavioralTranslatorL4_test.py
#=========================================================================
# Author : Peitian Pan
# Date   : May 28, 2019
"""Test the SystemVerilog translator implementation."""

import pytest

from pymtl3.passes.backends.verilog.util.utility import verilog_reserved
from pymtl3.passes.rtlir import BehavioralRTLIRGenPass, BehavioralRTLIRTypeCheckPass
from pymtl3.passes.rtlir.util.test_utility import expected_failure

from ....errors import VerilogTranslationError
from ....testcases import (
    CaseArrayBits32IfcInUpblkComp,
    CaseConnectValRdyIfcUpblkComp,
    CaseInterfaceArrayNonStaticIndexComp,
)
from ..VBehavioralTranslatorL4 import BehavioralRTLIRToVVisitorL4


def run_test( case, m ):
  m.elaborate()
  m.apply( BehavioralRTLIRGenPass( m ) )
  m.apply( BehavioralRTLIRTypeCheckPass( m ) )

  visitor = BehavioralRTLIRToVVisitorL4(lambda x: x in verilog_reserved)
  upblks = m._pass_behavioral_rtlir_gen.rtlir_upblks
  m_all_upblks = m.get_update_blocks()
  assert len(m_all_upblks) == 1

  for blk in m_all_upblks:
    upblk_src = visitor.enter( blk, upblks[blk] )
    upblk_src = "\n".join( upblk_src )
    assert upblk_src + '\n' == case.REF_UPBLK

@pytest.mark.parametrize(
    'case', [
      CaseConnectValRdyIfcUpblkComp,
      CaseArrayBits32IfcInUpblkComp,
      CaseInterfaceArrayNonStaticIndexComp,
    ]
)
def test_verilog_behavioral_L4( case ):
  run_test( case, case.DUT() )
