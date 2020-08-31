# User name lookup by IVBecy
##### Getting module(s)
import requests
import time
import sys

## Help
if sys.argv[1] == "-h":
  print("""
    Usage: spy.py [username]
    """)
  sys.exit()
# Input
uname = sys.argv[1]

##### Variables
# Sites
sites = {
    "Reddit": "https://www.reddit.com/user/",
    "Github": "https://github.com/",
    "Facebook": "https://www.facebook.com/",
    "Instagram": "https://www.instagram.com/",
    "Wordpress": "https://profiles.wordpress.org/",
    "Xbox": "https://xboxgamertag.com/search/",
    "Badoo": "https://badoo.com/",
    "Pinterest": "https://www.pinterest.com/",
    "SoundCloud": "https://soundcloud.com/",
    "TryHackMe": "https://tryhackme.com/p/",
    "Patreon": "https://www.patreon.com/",
    "CodePen": "https://codepen.io/",
    "PasteBin":"https://pastebin.com/u/",
    "Spotify":"https://open.spotify.com/user/",
    "Tellonym": "https://tellonym.me/",
    "Youtube": "https://www.youtube.com/",
    "AboutMe": "https://about.me/",
    "IFTT": "https://www.ifttt.com/p/",
    "MySpace": "https://myspace.com/",
    "PCPartPicker": "https://pcpartpicker.com/user/"
}

# Headers 
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

# Info
print("\n")
print("Username: " + uname)
print("\n")

#### Appending username to all sites + checking
for i in sites:
  sites[i] = sites[i] + uname
  req = requests.get(sites[i], headers=headers)
  if req.status_code == 200:
    print(f"[+] {i}: {sites[i]}")
  elif req.status_code == 404:
    print(f"[-] {i}: Not Found")
  else:
    print(f"[-] {i}: Error: {req.status_code}")
 


