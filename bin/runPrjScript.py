#!/usr/bin/python

from optparse import OptionParser
import sys
sys.path.append('/mnt/bin/lib')
from LibPrj import PrjTree

pt = PrjTree()
pt.listPrjScript()

