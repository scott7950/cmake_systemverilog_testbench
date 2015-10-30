#!/usr/bin/python

from optparse import OptionParser
import sys
sys.path.append('/mnt/bin')
from lib_run_test import BuildTree

usage = "Usage: %prog [options] arg1"
parser = OptionParser(usage=usage)
parser.add_option(
    "-b", "--build", action="store_true", dest="buildTree", default=False, help="Build Tree"
)
parser.add_option(
    "--bdir", dest="buildDir", default="TOT/build", metavar="FILE", help="Build Directory"
)
parser.add_option(
    "-c", "--compile", action="store_true", dest="compileProj", default=False, help="Compile Project"
)
(options, args) = parser.parse_args()

bt = BuildTree(options.buildDir)

if options.buildTree == True:
    bt.buildTree()

