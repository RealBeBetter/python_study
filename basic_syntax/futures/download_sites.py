import requests
import time


def download_one(url):
    resp = requests.get(url, timeout=20)
    if resp.status_code == 200:
        print('Read {} from {}'.format(len(resp.content), url))
    else:
        resp.raise_for_status()


def download_all(sites):
    for site in sites:
        download_one(site)


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

# Read 251067 from https://en.wikipedia.org/wiki/Portal:Arts
# Read 420788 from https://en.wikipedia.org/wiki/Portal:History
# Read 331715 from https://en.wikipedia.org/wiki/Portal:Society
# Read 1524357 from https://en.wikipedia.org/wiki/Portal:Biography
# Read 400189 from https://en.wikipedia.org/wiki/Portal:Mathematics
# Read 403939 from https://en.wikipedia.org/wiki/Portal:Technology
# Read 442944 from https://en.wikipedia.org/wiki/Portal:Geography
# Read 359184 from https://en.wikipedia.org/wiki/Portal:Science
# Read 424546 from https://en.wikipedia.org/wiki/Computer_science
# Read 634067 from https://en.wikipedia.org/wiki/Python_(programming_language)
# Read 353482 from https://en.wikipedia.org/wiki/Java_(programming_language)
# Read 668220 from https://en.wikipedia.org/wiki/PHP
# Read 214937 from https://en.wikipedia.org/wiki/Node.js
# Read 85262 from https://en.wikipedia.org/wiki/The_C_Programming_Language
# Read 383374 from https://en.wikipedia.org/wiki/Go_(programming_language)
# Download 15 sites in 18.897939100002986 seconds
