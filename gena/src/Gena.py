from Mistakes import Mistakes
from Data import Data
from Site import Site

class Gena():
    
    def __init__(self, input, output):
        self.input = input[:input.rfind('/'):] + "/"
        self.output = output + "/"
    
    def generate(self):
        
        if not Mistakes(self.input, self.output).get():
            Site(self.input, self.output, Data(self.input).get()).deploy()
            print(f"from {self.input} to {self.output}")
        