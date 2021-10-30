from PIL import Image
import requests
import os
import re
from hoshino import aiorequests,R
from asyncio import sleep
from datetime import datetime,timedelta
from hoshino import R, Service
from hoshino.typing import CQEvent, MessageSegment
from hoshino.util import FreqLimiter, DailyNumberLimiter
sv = Service('jiaran', enable_on_default=True, visible=False)
path='D:/jqr2/Leize_bot-master/hoshino/modules/jiaran/tupian/'#图片素材位置
path1=path+'g.png'#头像存放位置
path2=path+'1.png'#头像变原后存放位置
path3=path+'shou.png'
path4=path+'嘉然.png'
path5=path+'水滴.png'
path6=path+'ces.png'#最后生成的图片
def dow(url):
    resp = requests.get(url)
    f = open(path1, mode="wb")
    f.write(resp.content)
    f.close()
    pass
def yuan():
    image = Image.open(path1).convert("RGBA")
    ima = image.resize((130, 130), Image.ANTIALIAS)
    size = ima.size
    # 因为是要圆形，所以需要正方形的图片
    r2 = min(size[0], size[1])
    if size[0] != size[1]:
        ima = ima.resize((r2, r2), Image.ANTIALIAS)
    # 最后生成圆的半径
    r3 = int(r2 / 2)
    imb = Image.new('RGBA', (r3 * 2, r3 * 2), (255, 255, 255, 0))
    pima = ima.load()  # 像素的访问对象
    pimb = imb.load()
    r = float(r2 / 2)  # 圆心横坐标
    for i in range(r2):
        for j in range(r2):
            lx = abs(i - r)  # 到圆心距离的横坐标
            ly = abs(j - r)  # 到圆心距离的纵坐标
            l = (pow(lx, 2) + pow(ly, 2)) ** 0.5  # 三角函数 半径
            if l < r3:
                pimb[i - (r - r3), j - (r - r3)] = pima[i, j]
    imb.save(path2)
    pass
def ping():
    image4 = Image.open(path4).convert("RGBA")#本体
    image2 = Image.open(path2).convert("RGBA")#头像
    image3 = Image.open(path3).convert("RGBA")#手
    image5 = Image.open(path5).convert("RGBA") #水滴
    image2 = image2.resize((105, 105), Image.ANTIALIAS)
    final1 = Image.new("RGBA", image4.size)
    final1.paste(image4, (0, 0), image4)
    final1.paste(image2, (100, 210), image2)
    final1.paste(image3, (80, 260), image3)
    final1.paste(image5, (178, 210), image5)
    final1.save(path6)
    pass

@sv.on_rex(r'^嘉然头像(.*)')
async def jiar(bot, ev):
 obz=re.compile(r"嘉然头像(?P<name3>.*?)z",re.S)
 strr1=obz.search(str(ev.message)+"z")
 strr=strr1.group("name3")
 qq=strr
 url=f'http://q1.qlogo.cn/g?b=qq&nk={qq}&s=160'
 dow(url)
 yuan()
 ping()
 img=f"[CQ:image,file=file:///" + path6+ "]"
 await bot.send(ev, img)
 os.remove(path1) 
 os.remove(path2) 
 os.remove(path6)

