import os
import sys

class Mistake():
    
    def __init__(self, type, path, extension = '.json'):
        
        self.type = type
        self.path = path
        self.extension = extension
    
    def find(self):
        
        if self.type == 'folder':
            if not os.path.exists(self.path):
                print(f"Папки по пути {self.path} не существует")
                return True
        
        elif self.type == 'file':
            if not os.path.exists(self.path):
                print(f"файла по пути {self.path} не существует")
                return True
        
        elif self.type == 'extension':
            if os.path.splitext(self.path)[1] != self.extension:
               print(f"Расширение файла по пути {self.path} не {self.extension}") 
               return True
        
        elif self.type == 'rfolder':
            if os.path.exists(self.path + "site"):
                print(f"Папка по пути {self.path + 'images/site'} уже существует")
                return True
        return False
    