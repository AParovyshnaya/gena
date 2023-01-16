import tkinter as tk
from Button import Button

#class Interface():
#    
#    def __init__(self):
#        super().__init__()
#        pass
#    
#    def deploy(self):
#        
#        print(Button('file'))
#        Button('folder')
 
class Interface(): 
     
     def __init__(self):
         
         pass
     
     def deploy(self):
         
         window = tk.Tk()
         window.title('Gena')
         window.minsize(200, 150)
         window.iconbitmap("icon.ico")
         Button(window, 'file', 1).deploy()
         Button(window, 'dir', 2).deploy()
         label = tk.Label(window, text = "Я Гена")
         label.grid(column = 0, row = 0, columnspan = 7)
         window.mainloop()