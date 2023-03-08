class StandardItem():
    
    def __init__(self, value, standart = True):
        self.base = value
        self.standart = standart
        self.content = "<div class='container'><div class='row'><div class='col'>"
    
    def con(self):
        if self.standart:
            if self.base['visible']:
                inside = ''
                if self.base['visible_key']:
                    inside += self.base['name'] + ': '
                inside += self.base['value']
                self.content += inside
        else:
            self.content += self.base
        self.content += "</div></div></div>" 
        return self.content
        