from Images import Images
from Standart_Item import Standart_Item

class Item_Images():
    
    def __init__(self, input, output, base):
        self.input = input
        self.output = output
        self.base = base
        self.content = ''
    
    def content(self):
        for image in Images(self.base, self.input, self.output + 'site/').deploy():
            content += Standart_Item(image, standart = False).content()
        return content
    
        