import json
import os
import shutil
def enter():
    path = input("Абсолютный путь к папке с data.json и папкой images, содержащей папки ad и tech в корне (записывайте с '/'): ")
    path += "/"
    return path
def createSite():
    os.mkdir(path + "site")
    os.makedirs(path + "site/images")
    os.mkdir(path + "site/images/ad")
    os.mkdir(path + "site/images/tech")
    os.mkdir(path + "site/pages")
    os.mkdir(path + "site/pages/commodites")
def createCommodites():
    with open(path + 'data.json', encoding="UTF-8") as file:
        data = json.load(file)        
        commodities = data.get('commodity')
        return commodities
def genetateSite():
    index = open(path + "site/index.html", "w")
    for commodity in createCommodites():
        id = commodity.get("id")
        html = open(path + "site/pages/commodites/" + id[3:] + ".html", "w")
        html.write(f"<h1>{commodity.get('name')}</h1>")
        html.write(f"<p>{commodity.get('article')}</p>")
        price = commodity.get('price')
        html.write(f"<b>{price.get('value')}</b>")
        product = commodity.get('product')
        html.write(f"<p>Вес: {product.get('weight')} г</p>")
        if product.get('reserve') == 0:
            html.write("<p>Данного товара на складе нет</p>")
        else:
            html.write("<p>На складе есть этот товар</p>")
        story = commodity.get('adverting_story')    
        html.write(f"<p>{story.get('text')}</p>")
        image(story, 'adveting_photo', html)
        index.write(f"<div><a href={'pages/commodites/' + id[3:] + '.html'}><p><img src='{image(product, 'technical_photo', html)}' style='width: 300px'>{commodity.get('name')}</p></a></div>")      
def copyImage(src, id, name, ad_or_tech, html):
    old_path = path + src
    if not os.path.exists(old_path):
            print(f"Картинки по адресу {old_path} нет")
    else:
        exstension = os.path.splitext(old_path)[1]
        if exstension != ".jpeg" and exstension != ".png":
            print(f"Картинка по адресу {old_path} не соотвествует формату .png или .jpeg")
        else:
            new_path = "site/images/" + ad_or_tech + "/" + id[3:] + exstension
            html.write(f"<img src='{'../../' + new_path[5:]}' alt={name} style='width: 700px'>")
            new_path = path + new_path
            site_image = open(new_path, "w")
            shutil.copyfile(old_path, new_path)
            return "images/" + ad_or_tech + "/" + id[3:] + exstension
def image(object, name, html):
    images = object.get(name)
    if type(images) != list:
        print(f"У объекта {object} неккоректное значение свойства {name} ")
    elif images == [] and name == "technical_photo":
        print(f"У продукта {object} значение свойства {name} равно []")
    elif images != []:
        if name == "technical_photo":
            ad_or_tech = "tech"
        else:
            ad_or_tech = "ad"
        for image in images:
            return copyImage(image.get("src"), image.get("id"), image.get("name"), ad_or_tech, html)
        
path = enter()
#В виджетах
# темы - новогодняя и обычнаяE:/work/gena/git/gena/data
# help - что ждём от пользователей
if not os.path.isdir(path):
    print(f"Папки по пути {path} не существует")
elif not os.path.exists(path + 'data.json'):
    print(f"Файла по пути {path + 'data.json'} не существует")
elif not os.path.exists(path + 'images'):
    print(f"Папки по пути {path + 'images'} не существует")
elif not os.path.exists(path + 'images/ad'):
    print(f"Папки по пути {path + 'images/ad'} не существует")
elif not os.path.exists(path + 'images/tech'):
    print(f"Папки по пути {path + 'images/tech'} не существует")    
elif os.path.splitext(path + 'data.json')[1] != '.json':
    print("Расширение этого файла не .json")
elif os.path.exists(path + "site"):
     print(f"Папка по пути {path + 'images/site'} уже существует")
else:
    createSite()
    genetateSite()
    