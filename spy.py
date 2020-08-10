# User name lookup by IVBecy
##### Getting module(s)
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import sys

##### Variables
# Input
## Help
if sys.argv[1] == "-h":
  print("""
    Usage: spy.py [username]
    """)
  sys.exit()
uname = sys.argv[1] 
# Sites
sites = {
    "Reddit": "https://www.reddit.com/user/",
    "Github": "https://github.com/",
    "Facebook": "https://www.facebook.com/",
    "Instagram": "https://www.instagram.com/",
    "Twitter": "https://twitter.com/",
    "Twitch": "https://www.twitch.tv/",
    "Wordpress": "https://profiles.wordpress.org/",
    "Xbox": "https://xboxgamertag.com/search/",
    "Badoo": "https://badoo.com/",
    "Pinterest": "https://www.pinterest.com/",
    "Fiverr": "https://www.fiverr.com/",
    "TikTok": "https://www.tiktok.com/@",
    "SoundCloud": "https://soundcloud.com/",
    "R6Tab": "https://tabstats.com/siege/search/uplay/",
}
# Github uname check
notAllowed = [".","/","_","?","!",","]
state = "Pass"
# Sites that are needed to be individually looked through
exceptions = ["Github", "Reddit", "Twitter", "Badoo", "Xbox", "Fiverr", "TikTok", "SoundCloud", "R6Tab"]

###### Setting up the chrome driver
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')
print("\n")
print("Username:  " + uname)
print("\n")

#Checking for uname content (GITHUB)
for i in notAllowed:
  if i in uname:
    state = "Fail"

#### Appending username to all sites + checking
for i in sites:
  sites[i] = sites[i] + uname
  driver.get(sites[i])
  time.sleep(1) 
  ################### EXCEPTIONS ######################
  if i in exceptions:
      # GITHUB
    if i == "Github":
      # If the name contains anything from notAllowed
      if state == "Fail": 
        print("[-] " + i + ":" + " Not Found!")
      else:
        print("[+] " + i + ":" + " " + sites[i])
    #######################################
    # TWITTER
    elif i == "Twitter":
      try:
        # Look for background image
        if driver.find_element_by_class_name("css-9pa8cd"):
          print("[+] " + i + ":" + " " + sites[i])
      except NoSuchElementException:
        print("[-] " + i + ":" + " Not Found!")
    #######################################
    # REDDIT
    elif i == "Reddit":
      # Title of the page
      if "reddit: the front page of the internet" in driver.page_source:
          print("[-] " + i + ":" + " Not Found!")
      else:
        print("[+] " + i + ":" + " " + sites[i])
    #######################################
    # For BADOO
    elif i == "Badoo":
      # title of the page
      if "<title>Badoo" in driver.page_source:
          print("[-] " + i + ":" + " Not Found!")
      else:
        print("[+] " + i + ":" + " " + sites[i])
    #######################################
     # For XBOX
    elif i == "Xbox":
      # title of the page
      if "doesn't exist" in driver.page_source:
          print("[-] " + i + ":" + " Not Found!")
      else:
        print("[+] " + i + ":" + " " + sites[i])
    #######################################
     # For FIVERR
    elif i == "Fiverr":
      # title of the page
      if "no longer available" in driver.page_source:
          print("[-] " + i + ":" + " Not Found!")
      else:
        print("[+] " + i + ":" + " " + sites[i])
    #######################################
     # TIKTOK
    elif i == "TikTok":
      # title of the page
      try:
        # Look "4" from 404 error
        if driver.find_element_by_class_name("jsx-1194703849.jsx-1128529014"):
          print("[-] " + i + ":" + " Not Found!")
      except NoSuchElementException:
          print("[+] " + i + ":" + " " + sites[i])
     #######################################
     # SOUNDCLOUD
    elif i == "SoundCloud":
      try:
        # Look for "We cant find that user"
        if driver.find_element_by_class_name("errorTitle"):
          print("[-] " + i + ":" + " Not Found!")
      except NoSuchElementException:
          print("[+] " + i + ":" + " " + sites[i])
    #######################################
     # R6TAB
    elif i == "R6Tab":
      # Look for "We cant find that user"
      if "No profiles found" in driver.page_source:
        print("[-] " + i + ":" + " Not Found!")
      else:
         print("[+] " + i + ":" + " " + sites[i])
  #############################################################
  else:
    ### Not found pages detection (General pages [no exceptions])
    if "not found" in driver.page_source:
      print("[-] " + i + ":" +  " Not Found!" )

    elif "not-found" in driver.page_source:
      print("[-] " + i + ":" + " Not Found!")

    elif "Not Found" in driver.page_source:
      print("[-] " + i + ":" + " Not Found!")

    elif "Not-Found" in driver.page_source:
      print("[-] " + i + ":" + " Not Found!")

    else:
      print("[+] " + i + ":" + " " + sites[i])
print("\n")
driver.quit()


