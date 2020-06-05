#!/usr/local/bin/python
'''
   Autoplay manager for MPD.
   Loads set default playlist and exits if it's not playing.
   This is to supplement the auto-start feature in Moode
   because it might not always start playing on boot.
'''
from mpd import MPDClient

#------------------------------------
HOST = "localhost"
PORT = 6600
DEFAULT_PLAYLIST = "Bendra"
#------------------------------------

client = MPDClient()
try:
    client.connect(HOST, PORT)
except:
    print "[!] Connection to MPD failed"
    exit()

status = client.status()
if (status['state'] != "play"):
    print "[-] MPD not playing, loading playlist"
    client.clear()
    client.load(DEFAULT_PLAYLIST)
    client.random(1)
    client.play()
    client.close()
    client.disconnect()
    print "[+] Done!"
else:
    print "[+] MPD is already playing"
