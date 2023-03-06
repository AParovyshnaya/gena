from Item_Images import Item_Images

class Item_Story():
    
    def __init__(self, input, output, base):
        self.input = input
        self.output = output
        self.base = base
        self.content = "<div class='container'><div class='row'><div class='col>" + self.base['text'] + "</div></div></div>"
    
    def content(self):
        return content + Item_Images(self.input, self.output, self.base['adverting_photo'])