import shutil
from File import File

class Appendix():
    
    def __init__(self, input, output):
        
        self.input = input
        self.output = output
    
    def copy(self):
        
        File(self.output).deploy()
        shutil.copyfile(self.input, self.output)
        