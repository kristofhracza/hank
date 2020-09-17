# Getting module(s)
from requests import get
from sys import exit
from threading import Thread
from time import sleep
from optparse import OptionParser
from json import load


# method to be called when the user asks for help
def usage():
    print("""
  
    Usage: spy.py  -u [username] -f [file name]

    REQUIRED:
      -u or --username: your username

    OPTIONAL:
      -f or --file: the file to output the results into

  """)
    exit()


# Setting up the options for the terminal
parser = OptionParser()
parser.set_conflict_handler("resolve")
parser.add_option("-u", "--username", dest="uname")
parser.add_option("-h", "--help", dest="help", action="store_true")
parser.add_option("-f", "--file", dest="fileName")
(options, args) = parser.parse_args()

# If the username is set, the help menu cannot be shown (if called at the same time)
if options.uname:
    options.help = None

# Run the help menu
# If the username is not defined or the user asked for help
if options.uname is None or options.help:
    usage()

# Variables
# Loads sites from config.json file

with open("config.json") as config:
    sites = load(config)

# Headers 
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/50.0.2661.102 Safari/537.36 '
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


# Appending username to all sites + checking
def siteLookup(site, url):
    if site == "Twitter":
        req = get(url)
    else:
        req = get(url, headers=headers)
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


# Running the username check with threading
for j in range(2):
    for i in sites:
        sites[i] = sites[i].format(options.uname)
        thread = Thread(target=siteLookup, args=(i, sites[i],))
        thread.daemon = True
        thread.start()
        sleep(0.1)

for index in matchedSites:
    print(f"{index}: {matchedSites[index]}\n")
