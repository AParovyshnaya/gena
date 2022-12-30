import json
class Data():
    
    def __init__(self, input):
        self.input = input
    
    def get(self):
        with open(self.input + 'data.json', encoding="UTF-8") as file:
            data = json.load(file)        
            commodities = data.get('commodity')
            return commodities
        