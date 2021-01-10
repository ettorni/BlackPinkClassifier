import urllib
import flickrapi
from time import sleep


# First Argument is the key, Second is the secret code.
flickr = flickrapi.FlickrAPI('06b63685f13b1092b6fb3a5ffc4af6c5', 'ab2189bd936f41aa', cache=True)

# Getting the photos from flickr
jennie_photos = flickr.walk(text = 'blackpink jennie',
                     tag_mode = 'all',
                     tags = 'jennie',
                     extras = 'url_c',
                     per_page = 1000,
                     sort = 'relevance')

lisa_photos = flickr.walk(text = 'blackpink lisa',
                     tag_mode = 'all',
                     tags = 'lisa',
                     extras = 'url_c',
                     per_page = 1000,
                     sort = 'relevance')

jisoo_photos = flickr.walk(text = 'blackpink jisoo',
                     tag_mode = 'all',
                     tags = 'jisoo',
                     extras = 'url_c',
                     per_page = 1000,
                     sort = 'relevance')

rose_photos = flickr.walk(text = 'blackpink rose',
                     tag_mode = 'all',
                     tags = 'rose',
                     extras = 'url_c',
                     per_page = 1000,
                     sort = 'relevance')

jennie_urls = []
for i, photo in enumerate(jennie_photos):
    jennie_urls.append(photo.get('url_c'))
    if i > 1050:
        break

lisa_urls = []
for i, photo in enumerate(lisa_photos):
    lisa_urls.append(photo.get('url_c'))
    if i > 1050:
        break

jisoo_urls = []
for i, photo in enumerate(jisoo_photos):
    jisoo_urls.append(photo.get('url_c'))
    if i > 1050:
        break

rose_urls = []
for i, photo in enumerate(rose_photos):
    rose_urls.append(photo.get('url_c'))
    if i > 1050:
        break

jennie_urls = [x for x in jennie_urls if x is not None][:960]
lisa_urls = [x for x in lisa_urls if x is not None][:960]
jisoo_urls = [x for x in jisoo_urls if x is not None][:960]
rose_urls = [x for x in rose_urls if x is not None][:960]

# Downloading the images to folders
# Jennie Images
for count, url in enumerate(jennie_urls[:480]):
    urllib.request.urlretrieve(url, 'train/jennie/jennie' + str(count) + '.jpg')

sleep(120)

for count, url in enumerate(jennie_urls[480:]):
    urllib.request.urlretrieve(url, 'train/jennie/jennie' + str(480 + count) + '.jpg')

# Lisa Images
for count, url in enumerate(lisa_urls[:480]):
    urllib.request.urlretrieve(url, 'train/lisa/lisa' + str(count) + '.jpg')

sleep(120)

for count, url in enumerate(lisa_urls[480:]):
    urllib.request.urlretrieve(url, 'train/lisa/lisa' + str(450 + count) + '.jpg')

# Jisoo Images
for count, url in enumerate(jisoo_urls[:480]):
    urllib.request.urlretrieve(url, 'train/jisoo/jisoo' + str(count) + '.jpg')

sleep(120)

for count, url in enumerate(jisoo_urls[480:]):
    urllib.request.urlretrieve(url, 'train/jisoo/jisoo' + str(450 + count) + '.jpg')

# Rose Images
for count, url in enumerate(rose_urls[:480]):
    urllib.request.urlretrieve(url, 'train/rose/rose' +str(count) + '.jpg')

sleep(120)

for count, url in enumerate(rose_urls[480:]):
    urllib.request.urlretrieve(url, 'train/rose/rose' + str(450 + count) + '.jpg')

