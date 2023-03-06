class Item_Start():
    
    def __init__(self, value):
        self.value = value
    
    def content(self):
        return(f"<!DOCTYPE html><html><head><title>{self.value}</title><link rel='stylesheet' href='css/main.css'><meta charset='utf-8'></link><link rel='stylesheet' href='css/bootstrap.min.css'></link></head><body class='commodites body'><div class='header container text-center'><div class='row justify-content-md-center'><div class='col-md-auto'><a class='a' href='../../index.html'>Это Gena</a></div><div class='col-md-auto'><a class='a' href='../../index.html'><img src='../../images/site/icon.png'></a></div></div></a></div><div class='body container'><div class='container'><div class='row justify-content-md-center'><div class='col'>{self.value}</div></div></div>")