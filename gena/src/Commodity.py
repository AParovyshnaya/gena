import os
from File import File
from Images import Images
from Appendix import Appendix


class Commodity():
    
    def __init__(self, input, output, commodity):
        
        self.input = input
        self.output = output
        self.commodity = commodity
        
    def deploy(self):
        page = File(self.output + "site/pages/commodites/" + self.id + '.html').deploy()
        content, link = self.search(self.commodity)
        Appendix(os.getcwd().replace("\\", "/")[:os.getcwd().replace("\\", "/").rindex("/") + 1:] + 'src/files/css/bootstrap.min.css', self.output + "site/pages/commodites/css/bootstrap.min.css").copy()
        Appendix(os.getcwd().replace("\\", "/")[:os.getcwd().replace("\\", "/").rindex("/") + 1:] + 'src/files/css/main.css', self.output + "site/pages/commodites/css/main.css").copy()
        page.write(content + "</div></body></html>")
        return f"<div class='col-6'><a class='a' href={'pages/commodites/' + self.commodity['id']['value'][3:] + '.html'}><div class='col-4'><img src='{'images/tech' + self.commodity['product']['technical_photo'][0]['src'][self.technical_photo[0]['src'].rindex('/')::]}' style='width: 300px'></div><div class='col-2'>{self.commodity['name']}</div></a></div>"
    
    def check_key(self, key, base):
        if key == 'name':
            return False, self.start(key)
        if key == 'product':
            return False, self.search(base[key])
        elif key == 'adverting_story':
            return False, self.story(base['adverting_story'])
        elif key == 'technical_photo':
            return False, self.images(base[key])
        else:
            return True
    
    def start(self, name):
        return(f"<!DOCTYPE html><html><head><title>{name}</title><link rel='stylesheet' href='css/main.css'><meta charset='utf-8'></link><link rel='stylesheet' href='css/bootstrap.min.css'></link></head><body class='commodites body'><div class='header container text-center'><div class='row justify-content-md-center'><div class='col-md-auto'><a class='a' href='../../index.html'>Это Gena</a></div><div class='col-md-auto'><a class='a' href='../../index.html'><img src='../../images/site/icon.png'></a></div></div></a></div><div class='body container'><div class='container'><div class='row justify-content-md-center'><div class='col>{name}</div></div></div>")
    
    def story(self, base):
        content = "<div class='container'><div class='row'><div class='col>" + base['text'] + "</div></div></div>"
        return content + self.images(base['adverting_photo'])
    
    def images(self, base):
        content = ''
        for image in Images(base, self.input, self.output + 'site/').deploy():
            content += self.generate(image, standart = False)
        return content
        
    def generate(self, base, standart = True):
        content = "<div class='container'><div class='row'><div class='col>"
        if standart:
            if base['visible']:
                inside = base['value']
                if base['visible_header']:
                    inside += base['name']
                content += inside
        else:
            content += base
        return content + "</div></div></div>"   
    
    def search(self, base):
        content = ''
        for key, value in base.items():
            standart_key, add = self.check_key(key, base)
            content += add
            if standart_key:
                content += self.generate(value)
        return content
           