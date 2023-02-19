import sys
import os

class Image():
    def __init__(self):
        pass
    
    def check(self):
        if getattr(sys, 'frozen', False):
            return(os.path.join(sys._MEIPASS, "icons/icon.ico"))
        else:
            return("icons/icon.ico")