from Standart_Item import Standart_Item
from Item_Images import Item_Images
from Item_Story import Item_Story
from Item_Start import Item_Start

class Content_Item():
    
    def __init__(self, input, output, key, value):
        self.input = input
        self.output = output
        self.key = key
        self.value = value
        
    def content(self):
        if self.key == 'name':
            return False, Item_start(self.value).content()
        if self.key == 'product':
            return False, Content_Item(self.input, self.output, self.key, self.base).content()
        elif self.key == 'adverting_story':
            return False, Item_Story(self.input, self.output, self.value).content()
        elif self.key == 'technical_photo':
            return False, Item_Images(self.input, self.output, self.base).content
        else:
            return True, ''
    