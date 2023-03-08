from StandardItem import StandardItem
from ItemImages import ItemImages
from ItemStory import ItemStory
from ItemStart import ItemStart

class Content():
    def __init__(self, input, output):
        self.input = input
        self.output = output
        self.content = ''  
    
    def get_content(self, data):
        for key, value in data.items():
            standard_key, add = ContentItem(self.input, self.output, key, value).con()
            self.content += add
            if standard_key:
                self.content += StandardItem(value).con()
        return self.content
    
class ContentItem(Content):
    def __init__(self, input, output, key, value):
        self.input = input
        self.output = output
        self.key = key
        self.value = value
        self.content = ''
        
    def con(self):
        if self.key == 'name':
            return False, ItemStart(self.value).con()
        if self.key == 'product':
            return False, self.get_content(self.value)
        elif self.key == 'adverting_story':
            return False, ItemStory(self.input, self.output, self.value).con()
        elif self.key == 'technical_photo':
            return False, ItemImages(self.input, self.output, self.value).con()
        else:
            return True, ''
    