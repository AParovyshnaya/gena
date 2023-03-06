from Standart_Item import Standart_Item
from Content_Item import Content_Item

class Content():
    
    def __init__(self, input, output, data):
        self.input = input
        self.output = output
        self.data = data
        self.content = ''  
    
    def content(self):
        for key, value in self.data.items():
            standart_key, add = Content_Item(self.input, self.output, key, value).content()
            self.content += add
            if standart_key:
                self.content += Standart_Item(value).content()
        print(type(self.content))
        return self.content
           