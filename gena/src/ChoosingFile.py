import tkinter as tk
import tkinter.filedialog as fd

class File():
    
    def __init__(self, window, row):
        
        self.window = window
        self.row = row
        
    def deploy(self):
        
        def create():
            
            filetypes = (("Файл с данными", "*.json"), ('.json too)', '*.json'))
            print(fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes = filetypes))
        
        button = tk.Button(self.window, text = 'Открыть data.json', command = create)
        button.grid(column = 0, row = self.row)
        