import asyncio

import aiohttp
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'viewed="35217473"; bid=FCoiRmrrDHw; ll="118282"; douban-fav-remind=1; '
              'frodotk_db="0d60362ebc3d55d82820a28c34b80188"; ap_v=0,6.0'
}


def crawl_with_serial(url: str):
    content = requests.get(url, headers=headers, timeout=10).content
    soup = BeautifulSoup(content, 'html.parser')

    all_movies = soup.find("div", id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text

        response_item = requests.get(url_to_fetch, headers=headers, timeout=10).content
        soup_item = BeautifulSoup(response_item, 'html.parser')
        img_tag = soup_item.find('img')

        print(movie_name, url_to_fetch, movie_date, img_tag['src'])


async def fetch_content(url: str):
    async with aiohttp.ClientSession(headers=headers, connector=aiohttp.TCPConnector(ssl=False)
                                     ) as session:
        async with session.get(url) as response:
            return await response.text()


async def crawl_with_parallel(url: str):
    content = requests.get(url, headers=headers, timeout=10).content
    soup = BeautifulSoup(content, 'html.parser')

    movie_names, fetch_urls, movie_dates, img_tags = [], [], [], []

    all_movies = soup.find("div", id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_names.append(all_a_tag[1].text)
        fetch_urls.append(all_a_tag[1]['href'])
        movie_dates.append(all_li_tag[0].text)

    tasks = [fetch_content(url) for url in fetch_urls]
    pages = await asyncio.gather(*tasks)
    for page in pages:
        soup = BeautifulSoup(page, 'html.parser')
        img_tag = soup.find('img')
        img_tags.append(img_tag['src'])

    for i in range(len(movie_names)):
        print(movie_names[i], fetch_urls[i], movie_dates[i], img_tags[i])


# crawl_with_serial("https://movie.douban.com/cinema/later/shenzhen/")
asyncio.run(crawl_with_parallel("https://movie.douban.com/cinema/later/shenzhen/"))
