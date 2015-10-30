#!/usr/bin/python

import os
import re
import subprocess

class PrjTree:
    def __init__(self):
        self.bdir = 'TOT'
        self.TOTDir = None
        self.treeBin = None

    def listPrjScript(self):
        self.TOTDir = self.__findTOT()
        self.treeBin = self.TOTDir + '/bin'

        for dirname, dirnames, filenames in os.walk(self.treeBin):
            # print path to all subdirectories first.
            for subdirname in dirnames:
                print(os.path.join(dirname, subdirname))

            # print path to all filenames.
            for filename in filenames:
                print(os.path.join(dirname, filename))

            # Advanced usage:
            # editing the 'dirnames' list will stop os.walk() from recursing into there.
            if '.git' in dirnames:
                # don't go into any .git directories.
                dirnames.remove('.git')

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

