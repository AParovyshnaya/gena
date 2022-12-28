class Site():
    
    def __init__(self, output):
        self.output = output
        
    def deploy(self):
        print(f"Site.deploy(): {self.output}")
        