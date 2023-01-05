import os
from File import File
from Image import Image
from Appendix import Appendix

class Index():
    
    def __init__(self, input, output):
        
        self.input = input
        self.output = output
    
    def deploy(self):
        
        index = File(self.output + 'site/index.html').deploy()
        index.write("<!DOCTYPE html><html><head><title>gena</title><meta charset='utf-8'><meta name='viewport' content='width=device-width', initial-scale=1, shrink-to-fit='no'><link rel='stylesheet' href='css/main.css'></link><link rel='stylesheet' href='css/bootstrap.min.css'></link></head><body class='body'><div class='header container text-center'><div class='row justify-content-md-center'><div class='col-md-auto'><a class='a' href='index.html'>Это Gena</a></div><div class='col-md-auto'><a class='a' href='index.html'><img src='images/site/icon_64.png'></a></div></div></a></div><div class='body container'><div class='row'>")
        Image(self.input + 'images/site/phone.jpg', self.output + 'site/images/site/phone.jpg').deploy()
        Image(self.input + 'images/site/icon_64.png', self.output + 'site/images/site/icon_64.png').deploy()
        Appendix(os.getcwd().replace("\\", "/")[:os.getcwd().replace("\\", "/").rindex("/") + 1:] + 'files/css/bootstrap.min.css', self.output + "site/css/bootstrap.min.css").copy()
        Appendix(os.getcwd().replace("\\", "/")[:os.getcwd().replace("\\", "/").rindex("/") + 1:] + 'files/css/main.css', self.output + "site/css/main.css").copy()
        
        return index
    