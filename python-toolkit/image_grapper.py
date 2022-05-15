# image_grapper.py

from urllib.parse import urlencode
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import os
import aiohttp
import asyncio
import aiofiles


# constants
WALLPAPERS_KRAFT = 'https://wallpaperscraft.com/search/?'
WALLPAPERS_IMAGE_PATH = 'https://images.wallpaperscraft.com/image/'
usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

SAVE_DIR = './data/wallpaper/'

async def download_wallpapers_1080p(data, save_dir=SAVE_DIR):
    """
    Download wallpapers from https://wallpaperscraft.com and save in local dir
    """
    search = urlencode({'query': data})
    request = Request(WALLPAPERS_KRAFT + search, headers=usr_agent)
    r = urlopen(request).read()
    sew = BeautifulSoup(r, features='html.parser', from_encoding='GBK')

    cont = set()  # stores links of images
    for links in sew.find_all('a'):
        if '/wallpaper/' in links.get('href'):
            cont.add(links.get('href'))
    print('Search result: '  + str(len(cont)))
    if len(cont) == 0:
        return
    
    for c in cont:
        print(c)

    if not os.path.exists(save_dir):
      os.makedirs(save_dir)
   
    # # go to links and download high resolution images
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, re) for re in cont]
        await asyncio.gather(*tasks)
    
    return True

async def download_image(session, re):
    file_name = re[11:] + '_1280x720.jpg'
    async with session.get(WALLPAPERS_IMAGE_PATH + file_name) as response:
        data = await response.content.read()
        async with aiofiles.open(SAVE_DIR + file_name, 'wb') as file:
            await file.write(data)
            print(file_name + ' is downloaded')

async def main():
    # download wallpapers from
    data = input('Enter data to download wallpapers: ')
    await download_wallpapers_1080p(data)


if __name__ == "__main__":
    asyncio.run(main())
