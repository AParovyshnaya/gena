from Data import Data
from Site import Site

class Gena():
    
    def __init__(self, input, output):
        self.input = input
        self.output = output
    
    def generate(self):
        Data(self.input).get()
        Site(self.output).deploy()
        print(f"from {self.input} to {self.output}")
        