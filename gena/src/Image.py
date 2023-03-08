from Appendix import Appendix

class Image():
    
    def __init__(self, input, output, data = {'name': '', 'src': ''}):
        self.input = input
        self.output = output
        self.data = data
        self.name = self.data['name']
        self.src = self.data['src']
        if self.src != '':
            self.file = self.src[self.src.rindex('/')::]
            self.exstension = self.file[self.file.rindex('.')::]
        else:
            self.exstension = '.png'
    
    def deploy(self):
        Appendix(self.input + self.src, self.output + self.src).copy()
        
        if self.exstension != '.jpeg' and self.exstension != '.jpg' and self.exstension != '.png':
            print(f"Расширение изображения по адресу {self.output + self.src} не соостветсвует .png, .jpeg, .jpg")
        else:
            Appendix(self.input + self.src, self.output + self.src).copy()
            return f"<img class='img-fluid' src='{'../../' + self.src}' alt='{self.name}'>"
        