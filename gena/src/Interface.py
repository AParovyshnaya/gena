import tkinter as tk
from TargetFolder import TargetFolder
from DataFile import DataFile
from Trigger import Trigger
from ctypes import windll
from Check_image import Image
class Interface(): 
     def __init__(self):
         pass
     
     def deploy(self):
         windll.shcore.SetProcessDpiAwareness(1) 
         window = tk.Tk()
         window.title('Gena')
         window.minsize(200, 150)
         window.iconbitmap(Image().check())
         label = tk.Label(window, text = "Я Гена")
         description = tk.Label(window, text = "Сгенерирую вам сайт по файлу с данными формата '.json'.")
         label.grid(column = 0, row = 0, columnspan = 7)
         label.focus_set()
         description.grid(column = 0, row = 1)
         target = TargetFolder(window, 2)
         target.deploy()
         data = DataFile(window, 3)
         data.deploy()
         Trigger(window, 4, data, target).deploy()
         window.mainloop()
         return input, output
     