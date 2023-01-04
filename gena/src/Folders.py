from Folder import Folder

class Folders():
    
    def __init__(self, path):
        
        self.path = path
    
    def deploy(self):
        
        Folder(self.path + "site").deploy()
        Folder(self.path + "site/css").deploy()
        Folder(self.path + "site/images").deploy()
        Folder(self.path + "site/images/ad").deploy()
        Folder(self.path + "site/images/tech").deploy()
        Folder(self.path + "site/images/site").deploy()
        Folder(self.path + "site/pages").deploy()
        Folder(self.path + "site/pages/commodites").deploy()
        Folder(self.path + "site/pages/commodites/css").deploy()
    