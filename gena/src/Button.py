import tkinter as tk
import tkinter.filedialog as fd
from ChoosingFile import File
from ChoosingDir import Dir
class Button():
    
    def __init__(self, window, type, row):
        
        self.window = window
        self.type = type
        self.row = row
        
    def deploy(self):
        
        if self.type == 'file': 
            File(self.window, self.row).deploy()
        elif self.type == 'dir':
            Dir(self.window, self.row).deploy()    
            