import os
from File import File
from Images import Images
from Appendix import Appendix


class Commodity():
    
    def __init__(self, input, output, commodity):
        
        self.input = input
        self.output = output
        self.commodity = commodity
        self.name = self.commodity['name']
        self.id = self.commodity['id'][3::]
        self.article = self.commodity['article']
        self.product = self.commodity['product']
        self.weight = self.product['weight']
        self.reserve = self.product['reserve']
        if self.product['unit_of_measurement'] == 'grand':
            self.unit_of_measurement = 'шт.'
        elif self.product['unit_of_measurement'] == 'gram':
            self.unit_of_measurement = 'г.'
            self.reserve = self.reserve * self.weight
        self.technical_photo = self.product['technical_photo']
        self.image = self.technical_photo[0]['src'][self.technical_photo[0]['src'].rindex('/')::]
        self.price = self.commodity['price']['value']
        self.adverting_story = self.commodity['adverting_story']
        self.text = self.adverting_story['text']
        self.adverting_photo = self.adverting_story['adveting_photo']
        # что-то я делаю не так
        
    def deploy(self):
        
        page = File(self.output + "site/pages/commodites/" + self.id + '.html').deploy()
        
        def div(content, div_class='', head=False, center=False):
            
            if head:
                page.write(f"<!DOCTYPE html><html><head><title>{self.name}</title><link rel='stylesheet' href='css/main.css'><meta charset='utf-8'></link><link rel='stylesheet' href='css/bootstrap.min.css'></link></head><body class='commodites body'><div class='header container text-center'><div class='row justify-content-md-center'><div class='col-md-auto'><a class='a' href='../../index.html'>Это Gena</a></div><div class='col-md-auto'><a class='a' href='../../index.html'><img src='../../images/site/icon.png'></a></div></div></a></div><div class='body container'>")
            
            else:
                row_class = ''
                if center:
                    row_class = 'justify-content-md-center'
                page.write(f"<div class='container'><div class='row {row_class}'><div class='col {div_class}'>{content}</div></div></div>")
        
        div(self.name, head=True)
        div(self.name, center=True)
        div(self.article)
        div(self.price, div_class='price')
        div(str(self.weight) + " грамм") 
        div(str(self.reserve) + ' ' + self.unit_of_measurement)
        div(self.text)
        
        for image in Images(self.technical_photo, self.input, self.output + 'site/').deploy():
            
            div(image)
            
        for image in Images(self.adverting_photo, self.input, self.output + 'site/').deploy():
            
            div(image)
        
        Appendix(os.getcwd().replace("\\", "/")[:os.getcwd().replace("\\", "/").rindex("/") + 1:] + 'src/files/css/bootstrap.min.css', self.output + "site/pages/commodites/css/bootstrap.min.css").copy()
        Appendix(os.getcwd().replace("\\", "/")[:os.getcwd().replace("\\", "/").rindex("/") + 1:] + 'src/files/css/main.css', self.output + "site/pages/commodites/css/main.css").copy()
        
        page.write("</div></body></html>")
        return f"<div class='col-6'><a class='a' href={'pages/commodites/' + self.id + '.html'}><div class='col-4'><img src='{'images/tech' + self.image}' style='width: 300px'></div><div class='col-2'>{self.name}</div></a></div>"
    
