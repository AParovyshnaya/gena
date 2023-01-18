import tkinter as tk
from TargetFolder import TargetFolder
from DataFile import DataFile
from Trigger import Trigger
 
class Interface(): 
     
     def __init__(self):
         pass
     
     def deploy(self): 
         window = tk.Tk()
         window.title('Gena')
         window.minsize(200, 150)
         window.iconbitmap("icon.ico")
         label = tk.Label(window, text = "Я Гена")
         label.grid(column = 0, row = 0, columnspan = 7)
         target = TargetFolder(window, 1)
         target.deploy()
         data = DataFile(window, 2)
         data.deploy()
         Trigger(window, 3, data, target).deploy()
         window.mainloop()
         print(input, output)
         return input, output