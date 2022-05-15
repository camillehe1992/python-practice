# An example of crawling page

import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp

usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

def main_sequence(movies):
    
    for each_movie in movies:
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text

        response_item = requests.get(url_to_fetch, headers=usr_agent).content
        soup_item = BeautifulSoup(response_item, 'html.parser')
        img_tag = soup_item.find('img')

        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))


async def fetch_content(client, url):
    async with client.get(url) as response:
            return await response.text()

async def main_sync():
    movies = get_movies()
    movie_names, urls_to_fetch, movie_dates = [], [], []
    for each_movie in movies:
        name, url, date = parse_tag(each_movie)
        movie_names.append(name)
        urls_to_fetch.append(url)
        movie_dates.append(date)

    async with aiohttp.ClientSession() as client:
        tasks = [fetch_content(client, url) for url in urls_to_fetch]
        pages = await asyncio.gather(*tasks)

    for movie_name, movie_date, page in zip(movie_names, movie_dates, pages):
        soup_item = BeautifulSoup(page, 'html.parser', from_encoding='GBK')
        img_tag = soup_item.find('img')
        print('{} {} {}'.format(movie_name, movie_date, img_tag['arc']))

def get_movies():
    # sequence 
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = requests.get(url, headers=usr_agent).content
    init_soup = BeautifulSoup(init_page, 'html.parser')
    all_movies = init_soup.find('div', id='showing-soon')

    movies = all_movies.find_all('div', class_='item mod')
    movies += all_movies.find_all('div', class_='item mod odd')
    print(len(movies))
    return movies

def parse_tag(movie):
    all_a_tag = movie.find_all('a')
    all_li_tag = movie.find_all('li')

    return all_a_tag[1].text, all_a_tag[1]['href'], all_li_tag[0].text

if __name__ == "__main__":
    # main_sequence(movies)
    asyncio.run(main_sync())