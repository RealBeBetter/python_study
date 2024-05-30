import concurrent.futures
import requests
import time


def download_one(url):
    resp = requests.get(url, timeout=20)
    if resp.status_code == 200:
        print('Read {} from {}'.format(len(resp.content), url))
    else:
        resp.raise_for_status()


def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        todo_list = []
        for site in sites:
            future = executor.submit(download_one, site)
            todo_list.append(future)

        print('Waiting for all downloads to complete...')
        for future in concurrent.futures.as_completed(todo_list):
            future.result()


def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()
# Waiting for all downloads to complete...
# Read 333636 from https://en.wikipedia.org/wiki/Portal:Society
# Read 412723 from https://en.wikipedia.org/wiki/Computer_science
# Read 634154 from https://en.wikipedia.org/wiki/Python_(programming_language)
# Read 365672 from https://en.wikipedia.org/wiki/Portal:Science
# Read 380735 from https://en.wikipedia.org/wiki/Portal:Mathematics
# Read 214937 from https://en.wikipedia.org/wiki/Node.js
# Read 85072 from https://en.wikipedia.org/wiki/The_C_Programming_Language
# Read 1528529 from https://en.wikipedia.org/wiki/Portal:Biography
# Read 394374 from https://en.wikipedia.org/wiki/Portal:Technology
# Read 435865 from https://en.wikipedia.org/wiki/Portal:Geography
# Read 383048 from https://en.wikipedia.org/wiki/Go_(programming_language)
# Read 252229 from https://en.wikipedia.org/wiki/Portal:Arts
# Read 669742 from https://en.wikipedia.org/wiki/PHP
# Read 353482 from https://en.wikipedia.org/wiki/Java_(programming_language)
# Read 417597 from https://en.wikipedia.org/wiki/Portal:History
# Download 15 sites in 7.308305500017013 seconds
