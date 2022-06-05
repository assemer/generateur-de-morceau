#!/usr/bin/python3
from glob import glob
from random import randint as rq
from os import system as sys
from hashlib import md5 as m
import mutagen
from mutagen.oggopus import OggOpus
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4

# function to convert the information into 
# some readable format
def audio_duration(length):
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length  # calculate in seconds
  
    return mins, seconds  # returns the duration

  

json = "";



for fs in glob("musics/*"):

    musicFile = fs.replace("musics/", "")
    fileTypes = musicFile.split(".")[1]

    if fileTypes in "mp3":
        audio = MP3(fs)
    elif fileTypes in "opus":
        audio = OggOpus(fs)
    elif fileTypes in "m4a":
        audio = MP4(fs)


    audio_info = audio.info
    length = int(audio_info.length)
    mins, seconds = audio_duration(length)
    author =  musicFile.split('-')[0].upper()
    music = musicFile.split('-')[1].replace(".mp3", "").replace(".opus", "").replace(".m4a", "")[1:]
    mint,sec = str(rq(0,mins)), str(rq(0,60))
    musicHash = m(str(music+str(rq(0,10000))).encode("utf-8")).hexdigest()
    cmd = "ffmpeg -i '"+fs+"' -ss 00:"+mint+':'+sec+' -t 15 '+musicHash+'.mp3';

    json += '{"author":"'+author+'", "music" : "'+music+'", "Musicfile" : "'+musicHash+'.mp3","startingExtrectedOn" : "'+mint+':'+sec+'"},'
    sys(cmd)
 	


print(json)