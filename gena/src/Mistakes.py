from Mistake import Mistake

class Mistakes():
    
    def __init__(self, input, output):
        
        self.input = input
        self.output = output
    
    def get(self):
        
        def type(type, pathes):
            for path in pathes:
                if Mistake(type, path).find():
                    return True
            return False
    
        if type('folder', [self.input, self.input + 'images', self.input + 'images/ad', self.input + 'images/tech', self.input + 'images/site']) or type('file', [self.input + 'data.json']) or type('extension', [self.input + 'data.json']) or type('rfolder', [self.output + 'site']):
            return True
        return False
    