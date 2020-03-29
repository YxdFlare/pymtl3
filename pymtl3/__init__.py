from .datatypes import *
from .datatypes import _bitwidths
from .dsl.Component import Component
from .dsl.ComponentLevel1 import update
from .dsl.ComponentLevel2 import update_ff
from .dsl.ComponentLevel3 import connect
from .dsl.ComponentLevel4 import update_once
from .dsl.ComponentLevel5 import method_port
from .dsl.ComponentLevel6 import non_blocking
from .dsl.ComponentLevel7 import blocking
from .dsl.Connectable import (
    CalleeIfcCL,
    CalleeIfcFL,
    CalleeIfcRTL,
    CalleePort,
    CallerIfcCL,
    CallerIfcFL,
    CallerIfcRTL,
    CallerPort,
    InPort,
    Interface,
    OutPort,
    Wire,
)
from .dsl.ConstraintTypes import RD, WR, M, U
from .dsl.MetadataKey import MetadataKey
from .dsl.Placeholder import Placeholder
from .passes import TracingConfigs
from .passes.backends.verilog import (
    TranslationImportPass,
    VerilatorImportPass,
    VerilogTBGenPass,
)
from .passes.PassGroups import SimulationPass

__version__ = "0.5.8"

__all__ = [
  'U','M','RD','WR',
  'Wire', 'InPort', 'OutPort', 'Interface', 'CallerPort', 'CalleePort',
  'update', 'update_ff', 'update_once', 'connect', 'method_port',
  'CalleeIfcRTL', 'CallerIfcRTL',
  'non_blocking', 'CalleeIfcCL', 'CallerIfcCL',
  'blocking', 'CalleeIfcFL', 'CallerIfcFL',

  'SimulationPass', 'TracingConfigs', 'TranslationImportPass', 'VerilatorImportPass', 'VerilogTBGenPass',
  'Component', 'Placeholder',

  'trunc', 'sext', 'zext', 'clog2', 'concat', 'reduce_and', 'reduce_or', 'reduce_xor',
  'mk_bits', 'Bits',
  'mk_bitstruct', 'bitstruct',
] + [ "Bits{}".format(x) for x in _bitwidths ] \
  + [ "b{}".format(x) for x in _bitwidths ]
