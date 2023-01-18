import tkinter as tk
import tkinter.filedialog as fd

class TargetFolder():
    
    def __init__(self, window, row):
        self.window = window
        self.row = row
    
    def create(self):
        self.location = fd.askdirectory(title="Открыть папку", initialdir="/")  
    
    def path(self):
        return self.location
    
    def deploy(self):
        button = tk.Button(self.window, text = 'Открыть папку, в которой будет создан сайт', command = lambda: self.create())
        button.grid(column = 0, row = self.row)
        