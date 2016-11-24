__author__ = 'nico'


import MaxPlus

#MaxPlus.Core.WriteLine("hello world")

import sys
syspath = sys.path
for p in syspath: MaxPlus.Core.WriteLine(p)

sys.path.append(r"C:\YCDIVFX_MaxPlus-master\packages\maxviewport")
sys.path.append(r"C:\YCDIVFX_MaxPlus-master\packages")
sys.path.append(r"C:\YCDIVFX_MaxPlus-master\test")
sys.path.append(r"C:\YCDIVFX_MaxPlus-master\test\toto")

import maxviewport
reload(maxviewport)

syspath = sys.path
for p in syspath: MaxPlus.Core.WriteLine(p)
for item in sorted(sys.modules.keys()): print(item)

import test
reload(test)
from toto import toto6




test.toto.toto6.hello()

"""
#for item in sorted(sys.modules.keys()): print(item)
import maxviewport
reload(maxviewport)
"""