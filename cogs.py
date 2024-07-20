from PIL import Image, ImageDraw, ImageFont
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import json
import base64
import PIL

#smoothing corners for card and avtar
def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

#card minecraft user
def card_name(nick):
    f1 = requests.get(f'https://api.mojang.com/users/profiles/minecraft/' + nick)
    html1 = BS(f1.content, 'html.parser')

    json_load = json.loads(str(html1))
    id_json = json_load['id']
    f2 = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/' + id_json) 
    html2 = BS(f2.content, 'html.parser')

    data = json.loads(str(html2))
    url = base64.b64decode(str(data["properties"][0]['value']))
    dict = url.decode("ascii")

    dict = json.loads(dict)

    name_user = dict["profileName"]
    id_user = dict["profileId"]
    skin_url_user = dict["textures"]["SKIN"]["url"]


    img_url = Image.open(urlopen(f"{skin_url_user}"))
    img_url2 = Image.open(urlopen(f"{skin_url_user}"))

    img_url = img_url.crop((8, 8, img_url.width//4, img_url.height//4))
    img_url2 = img_url2.crop((40, 8, 48, 16))

    img1 = Image.alpha_composite(img_url, img_url2)
    img1 = img1.resize((512, 512), PIL.Image.NEAREST)

    pict1 = Image.new('RGB', (1920, 1080), (158, 195, 255))
    pict1.paste(img1,(50,50), add_corners(img1, 100))    
    pict1 = add_corners(pict1, 100)

    draw = ImageDraw.Draw(pict1)
    font = ImageFont.truetype(r"D:\GOTHAM-BLACK.TTF",  size = 128)
    font1 = ImageFont.truetype(r"D:\GOTHAM-BLACK.TTF",  size = 90)
    draw.text((600,100), "User: " + name_user, font = font, align="left")
    draw.text((75,600), "UUID: \n\n" + id_user, font = font1, align="left")
    pict1.save(f"lox.png")

#skin minecraft user
def skin_name(nick):
    f1 = requests.get(f'https://api.mojang.com/users/profiles/minecraft/' + nick)
    html1 = BS(f1.content, 'html.parser')

    json_load = json.loads(str(html1))
    id_json = json_load['id']
    f2 = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/' + id_json) 
    html2 = BS(f2.content, 'html.parser')

    data = json.loads(str(html2))
    url = base64.b64decode(str(data["properties"][0]['value']))
    dict = url.decode("ascii")

    dict = json.loads(dict)

    skin_url_user = dict["textures"]["SKIN"]["url"]
    img_url = Image.open(urlopen(f"{skin_url_user}"))
    img_url.save("skin.png")