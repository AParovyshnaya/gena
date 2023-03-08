from Images import Images
from StandardItem import StandardItem

class ItemImages():
    
    def __init__(self, input, output, base):
        self.input = input
        self.output = output
        self.base = base
        self.content = ''
    
    def con(self):
        for image in Images(self.base, self.input, self.output + 'site/').deploy():
            self.content += StandardItem(image, standart = False).con()
        return self.content
    
        