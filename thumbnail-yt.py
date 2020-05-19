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

    VIDEO_ID = re.search('watch\?v=(.*)',url).group(1)

    # This thumbnail always exists, so just show it up.
    hq_thumbnail = "https://i.ytimg.com/vi/%s/hqdefault.jpg" % (VIDEO_ID)
    print(hq_thumbnail)
    webbrowser.open(hq_thumbnail, new=2)

    max_thumbnail = "https://i.ytimg.com/vi/%s/maxresdefault.jpg" % (VIDEO_ID)
    # the max thumbnail not always exists, so I gotta check it.
    if not not_found(max_thumbnail,THUMBNAIL_NOT_FOUND):
      print(max_thumbnail)
      webbrowser.open(max_thumbnail, new=2)

if __name__ == '__main__':
  if len(sys.argv) == 1:
    print('./%s <yt url>' % sys.argv[0])
    exit()

  print('Be sure to remove the time variable (&t) at the end of the url')
  get_thumbnail(sys.argv[1])
