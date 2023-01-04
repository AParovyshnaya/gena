from Folders import Folders
from Commodity import Commodity
from Index import Index

class Site():
    
    def __init__(self, input, output, data):
        
        self.input = input
        self.output = output
        self.data = data
        
    def deploy(self):
        Folders(self.output).deploy()
        index = Index(self.input, self.output).deploy()
        for commodity in self.data:
            index.write(Commodity(self.input, self.output, commodity).deploy())
        index.write("</div></body></html>")
        