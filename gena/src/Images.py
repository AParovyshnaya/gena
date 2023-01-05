from Image import Image
from doctest import OutputChecker

class Images():
    
    def __init__(self, images, input, output):
        
        self.images = images
        self.input = input
        self.output = output
    
    def deploy(self):
        
        images_div = []
        
        for image in self.images:
            
            images_div.append(Image(self.input, self.output, data = image).deploy())
        
        return images_div    
            