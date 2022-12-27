import json
import os
import shutil
def enter():
    path = input("Абсолютный путь к папке с data.json и папкой images, содержащей папки ad и tech в корне : ").replace('\\', '/')
    print(path)
    path += "/"
    return path
def createSite():
    os.mkdir(path + "site")
    os.makedirs(path + "site/css")
    os.makedirs(path + "site/images")
    os.mkdir(path + "site/images/ad")
    os.mkdir(path + "site/images/tech")
    os.mkdir(path + "site/images/site")
    os.mkdir(path + "site/pages")
    os.mkdir(path + "site/pages/commodites")
def createCommodites():
    with open(path + 'data.json', encoding="UTF-8") as file:
        data = json.load(file)        
        commodities = data.get('commodity')
        return commodities
def createFile(adress, write='', old_adress='', our=False):
    new_path = path + adress
    file = open(new_path, "w", encoding="UTF-8")
    if our:
        old_path = os.getcwd().replace("\\", "/") + "/" + old_adress
        file = open(new_path, "w", encoding="UTF-8")
        shutil.copyfile(old_path, new_path)
    file.write(write)
    return file
def genetateSite():
    index = createFile("site/index.html", "<!DOCTYPE html><html><head><title>gena</title><meta charset='utf-8'><meta name='viewport' content='width=device-width', initial-scale=1, shrink-to-fit='no'><link rel='stylesheet' href='css/main.css'></link><link rel='stylesheet' href='css/bootstrap.min.css'></link></head><body><div class='header'><div>Это Gena</div><div><img src='images/site/icon.png'></div></div><div id='body'>")
    css = createFile("site/css/main.css", old_adress="files/css/main.css", our = True)
    bootsrap = createFile("site/css/bootstrap.min.css", old_adress="files/css/bootstrap.min.css", our = True)
    copyImage("images/site/phone.jpg", "phone", "phone", "site")
    copyImage("images/site/icon_64.png", "icon", "icon", "site")
    for commodity in createCommodites():
        id = commodity.get("id")
        html = createFile("site/pages/commodites/" + id[3:] + ".html", f"<!DOCTYPE html><html><head><title>{commodity.get('name')}</title><link rel='stylesheet' href='css/main.css'><meta charset='utf-8'></link><link rel='stylesheet' href='css/bootstrap.min.css'></link></head><body>")
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
        html.write("</body></html>")
    index.write("</div></body></html>")
def copyImage(src, id, alt, directory, html = '', cut = False):
    old_path = path + src
    if not os.path.exists(old_path):
            print(f"Картинки по адресу {old_path} нет")
    else:
        exstension = os.path.splitext(old_path)[1]
        if exstension != ".jpeg" and exstension != ".png" and exstension != ".jpg":
            print(f"Картинка по адресу {old_path} не соотвествует формату .png, .jpeg или .jpg")
        else:
            if cut:
                name = id[3:]
            else:
                name = id
            new_path = "site/images/" + directory + "/" + name + exstension
            if html != '':
                html.write(f"<img src='{'../../' + new_path[5:]}' alt='{alt}' style='width: 700px'>")
            new_path = path + new_path
            site_image = open(new_path, "w")
            shutil.copyfile(old_path, new_path)
            return "images/" + directory + "/" + name + exstension
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
            return copyImage(image.get("src"), image.get("id"), image.get("name"), ad_or_tech, html, True)
        
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
elif not os.path.exists(path + 'images/site'):
    print(f"Папки по пути {path + 'images/site'} не существует")   
elif os.path.splitext(path + 'data.json')[1] != '.json':
    print("Расширение этого файла не .json")
elif os.path.exists(path + "site"):
     print(f"Папка по пути {path + 'images/site'} уже существует")
else:
    createSite()
    genetateSite()
    