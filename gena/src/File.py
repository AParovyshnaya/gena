class File():
    
    def __init__(self, path):
        
        self.path = path
        
    def deploy(self):
        
        file = open(self.path, "w", encoding="UTF-8")
        return file
    