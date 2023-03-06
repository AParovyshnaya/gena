import os
from File import File
from Images import Images
from Appendix import Appendix
from Content import Content

class Commodity():
    
    def __init__(self, input, output, commodity):
        self.input = input
        self.output = output
        self.commodity = commodity
        self.id = self.commodity["id"]['value'][3:]
        
    def deploy(self):
        page = File(self.output + "site/pages/commodites/" + self.id + '.html').deploy()
        Appendix(os.getcwd().replace("\\", "/")[:os.getcwd().replace("\\", "/").rindex("/") + 1:] + 'src/files/css/bootstrap.min.css', self.output + "site/pages/commodites/css/bootstrap.min.css").copy()
        Appendix(os.getcwd().replace("\\", "/")[:os.getcwd().replace("\\", "/").rindex("/") + 1:] + 'src/files/css/main.css', self.output + "site/pages/commodites/css/main.css").copy()
        content_of_page = Content(self.input, self.output, self.commodity).content()
        page.write(content_of_page + "</div></body></html>")
        return f"<div class='col-6'><a class='a' href={'pages/commodites/' + self.id + '.html'}><div class='col-4'><img src='{'images/tech' + self.commodity['product']['technical_photo'][0]['src'][self.commodity['product']['technical_photo'][0]['src'].rindex('/')::]}' style='width: 300px'></div><div class='col-2'>{self.commodity['name']}</div></a></div>"