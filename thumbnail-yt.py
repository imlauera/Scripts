#!/usr/bin/env python3
import requests
import webbrowser
import sys
import re


def not_found(thumbnail,THUMBNAIL_NOT_FOUND):
    # If they are equal then that thumbnail doesn't exist.
    return requests.get(thumbnail).text == THUMBNAIL_NOT_FOUND


def get_thumbnail(url):
    # didn't find a better way to do it,lol
    THUMBNAIL_NOT_FOUND = requests.get('https://i.ytimg.com/vi/not_found/maxdefault.jpg').text

    r = requests.get(url)
    ID = re.search('watch\?v=(.*)',url).group(1)

    thumbnails = "https://i.ytimg.com/vi/%s/maxresdefault.jpg;https://i.ytimg.com/vi/%s/hqdefault.jpg" % (ID,ID)

    for thumbnail in thumbnails.split(';'):
      if not not_found(thumbnail,THUMBNAIL_NOT_FOUND):
        print(thumbnail)
        webbrowser.open(thumbnail, new=2)

if __name__ == '__main__':
  if len(sys.argv) == 1:
    print('./%s <yt url>' % sys.argv[0])
    exit()

  get_thumbnail(sys.argv[1])
