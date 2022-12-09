import json
import os.path

path = input("Абсолютный путь к файлу.json: ")

if os.path.exists(path) == False:
    print("Этого файла не существует")
elif os.path.splitext(path)[1] != '.json':
    print("Расширение этого файла не .json")
else:
    with open(path, encoding="UTF-8") as file:
        data = json.load(file)
        print(data)
