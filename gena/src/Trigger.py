import tkinter as tk
from Gena import Gena

class Trigger():
    
    def __init__(self, window, row, data, target_folder):
        self.window = window
        self.row = row
        self.data = data
        self.target_folder = target_folder
        
    def clicked(self):
        Gena(self.data.path(), self.target_folder.path()).generate()
    
    def deploy(self):
        button = tk.Button(self.window, text='Let`s start', command = self.clicked)
        button.grid(column = 0, row = self.row)
        