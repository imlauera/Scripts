# first install youtube-dl by doing. sudo pip3 install youtube-dl
# run youtube-dl -F https://www.youtube.com/watch?v=...  
# to see the available formats and youtube-dl -f <format_code> to choose one
# then run
youtube-dl -o - https://www.youtube.com/watch\?v\=xRzR3Th-5zE -f 140 | mpv -
# I've tried with mplayer and mpv both works great.
