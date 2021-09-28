Debug_Tag=1

def debug(log_msg):
    if(Debug_Tag) :
        print("DEBUG: " + log_msg)

from funcsigs import signature
import os
import vlc
import time

class mplayer:
    def __init__(self):
        self.inst = vlc.Instance()
        debug("instance created")
        self.plyr = self.inst.media_player_new()
        debug("player created")
        
    def playYoutube(self, URL):
        url = os.popen("youtube-dl -f best -g "+ URL).read().replace('\n', '')
        print(url)
        debug("grabbin' that steamy url")
        debug("URL:"+url)
        #media = self.inst.media_new(url)
        #debug("created media")
        self.plyr.set_mrl(url)
        debug("set mrl")
        self.plyr.play()
        debug("playing")

        #this might not work, especially if we try to implement a queue. 
        time.sleep(0.5)
        duration = self.plyr.get_length()
        time.sleep(duration)
        debug("sleeping till end of video")

def inputYoutube(playboi):
    print("please enter a youtube URL:")
    vidurl = raw_input()
    debug("INPUTTED URL: "+vidurl)
    debug("url captured hopefully")
    playboi.playYoutube(vidurl)
    debug("video played successfully, invalid url, or play youtube is broken")



def main():
    debug("Main function running")
    playboi = mplayer()
    debug("mplayer created successfully")

    print("Welcome to Media Controller")
    inputYoutube(playboi)
    debug("inputYoutube ran successfully or it is broken")
    nextVid = 1
    while(nextVid):
        print("would you like to watch another video?(y for yes, no is default)")
        stri = input()
        if(stri == "y"): nextVid = 1
        else: nextVid = 0
        if(nextVid):
            inputYoutube(playboi)
    debug("Main function ran successfully")

if(__name__=="__main__"):
    debug("Ran as main")
    main()
    exit()
