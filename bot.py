import os
import requests
import discord
import random
import csv
import pandas as pd
from datetime import datetime
from discord.ext import commands
from dotenv import load_dotenv
from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_SECRET')
TOKEN1= os.getenv('WEATHER_API')

base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Taipei"
complete_url = base_url + "appid=" + TOKEN1 + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    time=str(message.created_at)
    a=time[0:10]
    a=a.split("-")
    a="".join(a)
    a=datetime.strptime(a,"%Y%m%d").weekday()+1
    b=time[11:16]
    b=b[0:2]+b[3:5]
    c=list(b)
    if c[0]==0:
        c.remove(c[0])
        b=int("".join(c))
    else:
        b=int("".join(c))
    b=b+800
    if b>2400:
        b=b-2400
        a=a+1
    else:
        b=b
        
    d1=['早自習','音樂','體育','英文','英文','吃飯睡覺打手遊','美術','美術','打掃','物理','放學','下課']
    d2=['早自習','數學','數學','國文','國文','吃飯睡覺打手遊','班會','歷史','打掃','歷史','放學','下課']
    d3=['早自習','英文','英文','體育','化學','吃飯睡覺打手遊','耍廢','更廢','打掃','超廢','放學','下課']
    d4=['早自習','國文','國文','選修物理','選修物理','吃飯睡覺打手遊','音樂','數學','打掃','數學','放學','下課']
    d5=['早自習','基本設計','基本設計','多元選修','多元選修','吃飯睡覺打手遊','社團課','選修化學','打掃','選修化學','放學','下課']
    if a==1:
        if b<=810:
            k=d1[0]
            m=d1[1]
        if 810<b<=900:
            k=d1[1]
            m=d1[2]
        if 900<b<=910:
            k=d1[11]
            m=d1[2]
        if 910<b<=1000:
            k=d1[2]
            m=d1[3]
        if 1000<b<=1010:
            k=d1[11]
            m=d1[3]
        if 1010<b<=1100:
            k=d1[3]
            m=d1[4]
        if 1100<b<=1110:
            k=d1[11]
            m=d1[4]
        if 1110<b<=1200:
            k=d1[4]
            m=d1[5]
        if 1200<b<=1300:
            k=d1[5]
            m=d1[6]
        if 1300<b<=1350:
            k=d1[6]
            m=d1[7]
        if 1350<b<=1400:
            k=d1[11]
            m=d1[7]
        if 1400<b<=1450:
            k=d1[7]
            m=d1[8]
        if 1450<b<=1510:
            k=d1[8]
            m=d1[9]
        if 1510<b<=1600:
            k=d1[9]
            m=d1[10]
        if b>1600:
            k=d1[10]
            m=d1[10]
    if a==2:
        if b<=810:
            k=d2[0]
            m=d2[1]
        if 810<b<=900:
            k=d2[1]
            m=d2[2]
        if 900<b<=910:
            k=d2[11]    
            m=d2[2]
        if 910<b<=1000:
            k=d2[2]
            m=d2[3]
        if 1000<b<=1010:
            k=d2[11]
            m=d2[3]
        if 1010<b<=1100:
            k=d2[3]
            m=d2[4]
        if 1100<b<=1110:
            k=d2[11]
            m=d2[4]
        if 1110<b<=1200:
            k=d2[4]
            m=d2[5]
        if 1200<b<=1300:
            k=d2[5]
            m=d2[6]
        if 1300<b<=1350:
            k=d2[6]
            m=d2[7]
        if 1350<b<=1400:
            k=d2[11]
            m=d2[7]
        if 1400<b<=1450:
            k=d2[7]
            m=d2[8]
        if 1450<b<=1510:
            k=d2[8]
            m=d2[9]
        if 1510<b<=1600:
            k=d2[9]
            m=d2[10]
        if b>1600:
            k=d2[10]
            m=d2[10]
    if a==3:
        if b<=810:
            k=d3[0]
            m=d3[1]
        if 810<b<=900:
            k=d3[1]
            m=d3[2]
        if 900<b<=910:
            k=d3[11]
            m=d3[2]
        if 910<b<=1000:
            k=d3[2]
            m=d3[3]
        if 1000<b<=1010:
            k=d3[11]
            m=d3[3]
        if 1010<b<=1100:
            k=d3[3]
            m=d3[4]
        if 1100<b<=1110:
            k=d3[11]
            m=d3[4]
        if 1110<b<=1200:
            k=d3[4]
            m=d3[5]
        if 1200<b<=1300:
            k=d3[5]
            m=d3[6]
        if 1300<b<=1350:
            k=d3[6]
            m=d3[7]
        if 1350<b<=1400:
            k=d3[11]
            m=d3[7]
        if 1400<b<=1450:
            k=d3[7]
            m=d3[8]
        if 1450<b<=1510:
            k=d3[8]
            m=d3[9]
        if 1510<b<=1600:
            k=d3[9]
            m=d3[10]
        if b>1600:
            k=d3[10]
            m=d3[10]
    if a==4:
        if b<=810:
            k=d4[0]
            m=d4[1]
        if 810<b<=900:
            k=d4[1]
            m=d4[2]
        if 900<b<=910:
            k=d4[11]
            m=d4[2]
        if 910<b<=1000:
            k=d4[2]
            m=d4[3]
        if 1000<b<=1010:
            k=d4[11]
            m=d4[3]
        if 1010<b<=1100:
            k=d4[3]
            m=d4[4]
        if 1100<b<=1110:
            k=d4[11]
            m=d4[4]
        if 1110<b<=1200:
            k=d4[4]
            m=d4[5]
        if 1200<b<=1300:
            k=d4[5]
            m=d4[6]
        if 1300<b<=1350:
            k=d4[6]
            m=d4[7]
        if 1350<b<=1400:
            k=d4[11]
            m=d4[7]
        if 1400<b<=1450:
            k=d4[7]
            m=d4[8]
        if 1450<b<=1510:
            k=d4[8]
            m=d4[9]
        if 1510<b<=1600:
            k=d4[9]
            m=d4[10]
        if b>1600:
            k=d4[10]
            m=d4[10]
    if a==5:
        if b<=810:
            k=d5[0]
            m=d5[1]
        if 810<b<=900:
            k=d5[1]
            m=d5[2]
        if 900<b<=910:
            k=d5[11]
            m=d5[2]
        if 910<b<=1000:
            k=d5[2]
            m=d5[3]
        if 1000<b<=1010:
            k=d5[11]
            m=d5[3]
        if 1010<b<=1100:
            k=d5[3]
            m=d5[4]
        if 1100<b<=1110:
            k=d5[11]
            m=d5[4]
        if 1110<b<=1200:
            k=d5[4]
            m=d5[5]
        if 1200<b<=1300:
            k=d5[5]
            m=d5[6]
        if 1300<b<=1350:
            k=d5[6]
            m=d5[7]
        if 1350<b<=1400:
            k=d5[11]
            m=d5[7]
        if 1400<b<=1450:
            k=d5[7]
            m=d5[8]
        if 1450<b<=1510:
            k=d5[8]
            m=d5[9]
        if 1510<b<=1600:
            k=d5[9]
            m=d5[10]
        if b>1600:
            k=d5[10]
            m=d5[10]
    if a>5:
        k='睡覺'
        m='耍廢'

    if message.content == '$課表':
        await message.channel.send('現在是'+datetime.now().strftime('%m月%d日 %H:%M'))
        await message.channel.send('現在是:'+k+'時間')
        await message.channel.send('接下來是:'+m+'時間')

    if message.content == '$天氣':
        await message.channel.send(" 溫度= " +
                    str(current_temperature-273.15)[0:4]+'°C' +
        "\n 大氣壓力= " +
                    str(current_pressure)+' hPa'+
        "\n 濕度= " +
                    str(current_humidity) +'%'+
        "\n 天氣=  " +
                    str(weather_description))

    if message.content == '$圖':
        path="D:/USER/Documents/GitHub/Code/Python/Discord/pics"
        files=os.listdir(path)
        d=random.choice(files)
        picture = discord.File(path+'/'+d)
        await message.channel.send(file=picture)

    if message.content == '$h':
        path="D:/USER/Documents/GitHub/Code/Python/Discord/picsh"
        files=os.listdir(path)
        d=random.choice(files)
        picture = discord.File(path+'/'+d)
        await message.channel.send(file=picture)

    if message.content.startswith('$地點'):
            locator = Nominatim(user_agent='name_of_your_app')
            geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
            a = str(message.content)[4:]
            location = locator.geocode(a)
            addr = location.address
            lat_lon = location.latitude, location.longitude
            await message.channel.send(addr+"\n"+str(lat_lon))

    if message.content=='$help':
        embed=discord.Embed(title="指令介紹", url="https://ethane1755.github.io/",description="⬆歡迎關注窩的網站", color=0x61afef)
        embed.set_author(name=message.author.display_name, url="https://ethane1755.github.io/", icon_url="https://i.postimg.cc/4xLzfTHq/15000971312403.jpg")
        embed.add_field(name="$課表", value="現在時間、目前課程、下一節課程", inline=False)
        embed.add_field(name="$天氣(以台北市為準)", value="輸出溫度、大氣壓力、濕度、天氣概述", inline=False) 
        embed.add_field(name="$地點{地點，中英文皆可}", value="輸出地址、經緯度 \n ex:$地點 中正紀念堂", inline=False) 
        embed.add_field(name="$圖", value="來自Pixiv的香圖，有推薦圖庫歡迎私訊", inline=False) 
        embed.add_field(name="$h", value="慎用!!!來自Pixiv的色圖，有推薦圖庫歡迎私訊", inline=False) 
        embed.add_field(name="$t{事件}{日期(YYYYMMDD)}", value="輸入接下來的排程\n ex:$t 國慶日 20221010", inline=False)
        embed.add_field(name="$k", value="查看倒數、今日須辦事項", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith('$t'):
        initial=message.content[3:-8]
        time=message.content[-8:]
        with open('data.csv', 'a', newline='',encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([initial,time])
        test=pd.read_csv('data.csv', index_col=0, header=None, squeeze=True,encoding='utf-8').to_dict()
        now=datetime.now()
        d1={}
        d2={}
        for key, value in test.items():
            initial=datetime.strptime(str(value),'%Y%m%d')
            k=(initial-now).days+1
            if k>0:
                d1[key]=k
            if k==0:
                d2[key]=k
        await message.channel.send('今日待辦事項:\n')
        d2={k: v for k, v in sorted(d2.items(), key=lambda item: item[1])}
        for key in d2:
            p3=str(key)
            p4=str(d2[key])
            await message.channel.send(p3)
        await message.channel.send('其他待辦事項:\n')
        d1={k: v for k, v in sorted(d1.items(), key=lambda item: item[1])}
        for key in d1:
            p=str(key)
            p1=str(d1[key])
            await message.channel.send(p+' -- '+p1+'天')
    if message.content.startswith('$k'):
        test=pd.read_csv('data.csv', index_col=0, header=None, squeeze=True,encoding='utf-8').to_dict()
        now=datetime.now()
        d1={}
        d2={}
        for key, value in test.items():
            initial=datetime.strptime(str(value),'%Y%m%d')
            k=(initial-now).days+1
            if k>0:
                d1[key]=k
            if k==0:
                d2[key]=k
        d2={k: v for k, v in sorted(d2.items(), key=lambda item: item[1])}
        await message.channel.send('今日待辦事項:\n')
        for key in d2:
            p3=str(key)
            await message.channel.send(p3)
        await message.channel.send('其他待辦事項:\n')
        d1={k: v for k, v in sorted(d1.items(), key=lambda item: item[1])}
        for key in d1:
            p=str(key)
            p1=str(d1[key])
            await message.channel.send(p+' -- '+p1+'天')

client.run(TOKEN,reconnect=True)
