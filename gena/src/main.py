from Gena import Gena
from Interface import Interface

Interface().deploy()    
Gena(input("Папка, в которой лежит data.json: "), input("Папка, в которой будет сайт: ")).generate()
