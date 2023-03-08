from ItemImages import ItemImages

class ItemStory():
    
    def __init__(self, input, output, base):
        self.input = input
        self.output = output
        self.base = base
        self.content = "<div class='container'><div class='row'><div class='col>" + self.base['text'] + "</div></div></div>"
    
    def con(self):
        return self.content + ItemImages(self.input, self.output, self.base['adverting_photo']).con()