import os

class Folder():
    def __init__(self, path):
        self.path = path
    
    def deploy(self):
        os.mkdir(self.path)
            