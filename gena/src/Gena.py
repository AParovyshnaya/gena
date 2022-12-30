from Mistakes import Mistakes
from Data import Data
from Site import Site

class Gena():
    
    def __init__(self, input, output):
        self.input = input.replace('\\', '/') + "/"
        self.output = output.replace('\\', '/') + "/"
    
    def generate(self):
        if not Mistackes(self.input, self.output).get():
            Data(self.input).get()
            Site(self.output).deploy()
            print(f"from {self.input} to {self.output}")
        