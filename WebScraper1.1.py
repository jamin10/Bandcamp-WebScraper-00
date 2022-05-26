# Bandcamp Webscraper v1.0

import requests
from bs4 import BeautifulSoup

# send request for webpage HTML
wisdomteeth_response = requests.get('https://wisdomteethuk.bandcamp.com/')
wisdomteeth = wisdomteeth_response.content

# convert HTML to BeautifulSoup object
wisdomteeth_soup = BeautifulSoup(wisdomteeth, "html.parser")

# Find all elements with class=title and add to a list
title_list = []
artist_list = []
for release in wisdomteeth_soup.find_all(attrs={'class':'title'}):
    # Split up elements into a list
    release_text = release.get_text('|').split('|')
    if len(release_text) > 1:
        title_list.append(release_text[0])
        artist_list.append(release_text[1])
    else:
        title_list.append((release_text[0]))
        artist_list.append("none")

print(artist_list)

title_list_cleaned = []
for el in title_list:
    title_list_cleaned.append(el.strip())


while("" in title_list_cleaned):
    title_list.remove("")

title_list_cleaned = title_list_cleaned[:-4]
# release_list.remove(release_list[-4:])

print(title_list_cleaned)

