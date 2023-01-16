import tkinter as tk
import tkinter.filedialog as fd

class Dir():
    
    def __init__(self, window, row):
        
        self.window = window
        self.row = row
    
    def deploy(self):
        
        def create():
            
            directory = fd.askdirectory(title="Открыть папку", initialdir="/")
            print(directory)
            
        button = tk.Button(self.window, text = 'Открыть папку, в которой будет создан сайт', command = create)
        button.grid(column = 0, row = self.row)