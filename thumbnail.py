#!/usr/bin/env python3
import requests
import webbrowser
import sys
import re

# didn't find a better way to do it,lol
THUMBNAIL_NOT_FOUND = requests.get('https://i.ytimg.com/vi/not_found/maxdefault.jpg').text

def not_found(thumbnail):
    # If they are equal then that thumbnail doesn't exist.
    return requests.get(thumbnail).text == THUMBNAIL_NOT_FOUND


def get_thumbnail(url):
    r = requests.get(url)
    ID = re.search('watch\?v=(.*)',url).group(1)

    thumbnails = "https://i.ytimg.com/vi/%s/maxresdefault.jpg;https://i.ytimg.com/vi/%s/hqdefault.jpg" % (ID,ID)

    for thumbnail in thumbnails.split(';'):
      if not not_found(thumbnail):
        print(thumbnail)
        webbrowser.open(thumbnail, new=2)

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('%s <yt url>') % sys.argv[0]

  get_thumbnail(sys.argv[1])
