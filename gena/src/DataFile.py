import tkinter as tk
import tkinter.filedialog as fd

class DataFile():
    
    def __init__(self, window, row):
        self.window = window
        self.row = row
        
    def create(self):
        filetypes = (("Файл с данными", "*.json"), ('.json too)', '*.json'))
        self.location = fd.askopenfilename(title="Открыть файл", filetypes = filetypes)
        
    def deploy(self):
        button = tk.Button(self.window, text = 'Открыть data.json', command = lambda: self.create())
        button.grid(column = 0, row = self.row)
    
    def path(self):
        return self.location
    