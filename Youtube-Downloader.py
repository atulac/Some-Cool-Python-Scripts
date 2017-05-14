import os
from subprocess import call

path='' #put the path to which you want the playlist videos to be downloaded

backslash_map = { '\a': r'\a', '\b': r'\b', '\f': r'\f',
                  '\n': r'\n', '\r': r'\r', '\t': r'\t', '\v': r'\v' }

for key,value in backslash_map.items():
        path=path.replace(key,value)

os.chdir(path)			#change current directory to your path

call('dir',shell=True)

command="youtube-dl --playlist-start 1 "    #Replace 1 with the video number you want to start downloading

command+='"https://www.youtube.com/watch?v=DKOLynNhWxo&list=RDQMZfvcdmWTukM&index=1"'  #link of the starting video

call(command,shell=True)

raw_input("press enter to exit ;)") 
#--playlist-start 5
