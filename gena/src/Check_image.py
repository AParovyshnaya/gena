import sys
class Image():
    def __init__(self):
        pass
    
    def check(self):
        if getattr(sys, 'frozen', False):
            return(os.path.join(sys._MEIPASS, "icon.ico"))
        else:
            return("icon.ico")