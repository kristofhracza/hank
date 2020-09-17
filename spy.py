##### Getting module(s)
import requests
import sys
import threading
import time
from optparse import OptionParser

# method to be called when the user asks for help
def usage():
  print("""
  
    Usage: spy.py  -u [username] -f [file name]

    REQUIRED:
      -u or --username: Username of the victim

    OPTIONAL:
      -f or --file: the file to output the results into

  """)
  sys.exit()

#Setting up the options for the terminal
parser = OptionParser()
parser.set_conflict_handler("resolve")
parser.add_option("-u", "--username",dest="uname")
parser.add_option("-h", "--help", dest="help", action="store_true")
parser.add_option("-f", "--file", dest="fileName")
(options, args) = parser.parse_args()

# If the username is set, the help menu cannot be shown (if called at the same time)
if options.uname:
  options.help = None

# Run the help menu
### If the username is not defined
if options.uname == None:
  usage()
### If the user has asked for help
if options.help:
  usage()

##### Variables
# Sites
sites = {
  "AboutMe": "https://about.me/{}",
  "Badoo": "https://badoo.com/{}",
  "BitBucket": "https://bitbucket.org/{}",
  "Chess": "https://www.chess.com/member/{}",
  "Codecademy": "https://www.codecademy.com/profiles/{}",
  "CodePen": "https://codepen.io/{}",
  "DevCommunity": "https://dev.to/{}",
  "Discogs": "https://www.discogs.com/user/{}",
  "Ello": "https://ello.co/{}",
  "Github": "https://github.com/{}",
  "IFTTT": "https://www.ifttt.com/p/{}",
  "Instagram": "https://www.instagram.com/{}",
  "Keybase": "https://keybase.io/{}",
  "MySpace": "https://myspace.com/{}",
  "PasteBin": "https://pastebin.com/u/{}",
  "Patreon": "https://www.patreon.com/{}",
  "PCPartPicker": "https://pcpartpicker.com/user/{}",
  "Pinterest": "https://www.pinterest.com/{}",
  "Reddit": "https://www.reddit.com/user/{}",
  "SourceForge": "https://sourceforge.net/u/{}",
  "SoundCloud": "https://soundcloud.com/{}",
  "Spotify": "https://open.spotify.com/user/{}",
  "Tellonym": "https://tellonym.me/{}",
  "TryHackMe": "https://tryhackme.com/p/{}",
  "Twitch": "https://m.twitch.tv/{}",
  "Twitter": "https://mobile.twitter.com/{}",
  "Unsplash": "https://unsplash.com/@{}",
  "Wordpress": "https://profiles.wordpress.org/{}",
  "Xbox": "https://xboxgamertag.com/search/{}",
  "Youtube": "https://www.youtube.com/{}",
}

# Headers 
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

matchedSites = {}

# Info
print("""
 _____                               
/  ___|                              
\ `--. _ __  _   _       _ __  _   _ 
 `--. \ '_ \| | | |     | '_ \| | | |
/\__/ / |_) | |_| |  _  | |_) | |_| |
\____/| .__/ \__, | (_) | .__/ \__, |
      | |     __/ |     | |     __/ |
      |_|    |___/      |_|    |___/ 
      
""")
print(f"Username: {options.uname}")
print("\n")

#### Appending username to all sites + checking
def siteLookup(site, url):
  if site == "Twitter":
    req = requests.get(url)
  else:
    req = requests.get(url, headers=headers)
  if req.status_code == 200:
    if site in matchedSites.values():
      pass
    else:
      matchedSites[site] = url
    # If we need to write to a file
    if options.fileName:
      f = open(options.fileName, "a")
      f.write(f"{site}: {url}")
      f.write("\n")

#Running the username check with threading
for i in range(2):
  for i in sites:
    sites[i] = sites[i].format(options.uname)
    thread = threading.Thread(target=siteLookup, args=(i,sites[i],))
    thread.daemon = True
    thread.start()
    time.sleep(0.1)

for index in matchedSites:
  print(f"{index}: {matchedSites[index]}")
print("\n")



