#!/usr/bin/bash
if [ ! "$(command -v feh)" ]; then echo "bro, you need to install feh"; exit; fi

# RATING: questionable, explicit, safe
RATING="questionable"
RESOLUTION=$(xrandr | grep '*' | awk '{print $1}') &&
WIDTH=$(echo $RESOLUTION | cut -d 'x' -f 1) &&
HEIGHT=$(echo $RESOLUTION | cut -d 'x' -f 2) &&
echo "Your resolution is $WIDTH x $HEIGHT" &&
GET_WALL=$(curl -s https://konachan.com/post.json\?tags\=%20width:$WIDTH%20height:$HEIGHT%20order:wide%20rating:$RATING%20order:random limit:1 | 
	 jq -r '.[0]["file_url"]') &&
echo "Downloading and setting wallpaper" &&
feh --bg-max $GET_WALL &&
echo "Done"
