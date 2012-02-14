__author__ = 'vangelis'

import subprocess

class Application:
    def __init__(self):
        self.execCommand = "mpirun -np 4 "
        self.process = None
        self.inputData = {}
        self.outputData = {}

    def run(self):
        if self.execCommand is not None:
            process = subprocess.Popen(self.execCommand, shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
            return process
        else:
            return None

    def poll(self):
        return self.process.poll()

    def kill(self):
        if self.process is not None:
            self.process.kill()
            return True
        else:
            return False

    def setInputData(self, dataref):
        if dataref is not None and dataref not in self.inputData:
            self.inputData.add(dataref)
            return True
        else:
            return False

    def setOutputData(self, dataref):
        if dataref is not None and dataref not in self.outputData:
            self.outputData.add(dataref)
            return True
        else:
            return False




    