#!/usr/bin/python

from optparse import OptionParser
import sys
sys.path.append('/mnt/bin/lib')
from LibPrj import PrjTree

print sys.argv

prjScriptCmd = ""
if len(sys.argv) >= 2:
    for argv in sys.argv[1:]:
        prjScriptCmd += " " + argv

pt = PrjTree()
pt.listPrjScript()
pt.runPrjScript(prjScriptCmd)

