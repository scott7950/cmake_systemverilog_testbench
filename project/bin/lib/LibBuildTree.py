#!/usr/bin/python

import os
import re
import subprocess

class BuildTree:
    def __init__(self, bdir):
        self.bdir = bdir
        self.TOTDir = None

    def buildTree(self):
        self.TOTDir = self.__findTOT()
        self.__replaceTOT()
        if not os.path.exists(self.bdir):
            os.mkdir(self.bdir)
        os.chdir(self.bdir)
        subprocess.call(["cmake", self.TOTDir])

    def compileProj(self):
        subprocess.call(["make", "compile"])

    def __findTOT(self):
        cwd = os.getcwd()

        while(cwd != "/"):
            if os.path.exists(cwd + "/TOT"):
                cwd = re.sub(r'/$', r'', cwd)
                return cwd
            cwd = re.sub(r'\w+(?:/)?$', r'', cwd)

        raise Exception('There is no TOT in path ' + os.getcwd())

    def __replaceTOT(self):
        result = re.subn(r'\bTOT\b', self.TOTDir, self.bdir)
        if result[1] > 1:
            raise Exception('More than 1 TOT in provided build directory' + self.bdir)

        self.bdir = result[0]

