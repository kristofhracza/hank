##### Getting module(s)
import requests
import sys
import threading
import time
import json
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

# Setting up the options for the terminal
parser = OptionParser()
parser.set_conflict_handler("resolve")
parser.add_option("-u", "--username",dest="uname")
parser.add_option("-h", "--help", dest="help", action="store_true")
parser.add_option("-f", "--file", dest="fileName")
(options, args) = parser.parse_args()

# Run the help menu
### If the username is not defined
if options.uname == None or options.help:
  usage()
# If the username is set, the help menu cannot be shown (if called at the same time)
if options.uname:
  options.help = None

##### Variables
# Sites from the json file
with open("sites.json") as config:
  sites = json.load(config)

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
print(f"Username: {options.uname}\n")

#### Appending username to all sites + checking
def siteLookup(site, url):
  try:
    if site == "Twitter":
      req = requests.get(url)
    else:
      req = requests.get(url, headers=headers)
    if req.status_code == 200:
      if site in matchedSites.values():
        pass
      else:
        matchedSites[site] = url
  # on SSL error if the website is blocked
  except requests.exceptions.SSLError:
    print(f"[!] {site} is unreachable, might be blocked")
#Running the username check with threading
for iterator in range(2):
  for i in sites:
    sites[i] = sites[i].format(options.uname)
    thread = threading.Thread(target=siteLookup, args=(i,sites[i],))
    thread.daemon = True
    thread.start()
    time.sleep(0.1)

# Loop through the found sites
print(f"\nUsername: {options.uname} found at {len(matchedSites)} sites\n")
for index in matchedSites:
  print(f"{index}: {matchedSites[index]}")
  # If we need to write to a file
  if options.fileName:
    f = open(options.fileName, "a")
    f.write(f"{index}: {matchedSites[index]}\n")
print("\n")