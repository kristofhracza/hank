from lib.setup import *
from random import choice

# Main variables
SITES,OPTIONS = make()
matched_sites = {}


# Query sites
def site_lookup():
  for site in SITES:
    url = SITES[site].format(OPTIONS.user_name)
    try:
      req = requests.get(url, headers={"User-Agent":choice(UA)},allow_redirects=False)
      if req.status_code == 200:
          matched_sites[site] = url
      if OPTIONS.verbose:
        print(f"[*] {site}:\t{url}")
    except requests.exceptions.SSLError:
      if OPTIONS.verbose:
        print(f"[!]{url} -- requests.exceptions.SSLError")
    

# Logging
def site_log():
  for index in matched_sites:
    print(f"{index}:\t{matched_sites[index]}")
    if OPTIONS.file_name:
      f = open(OPTIONS.file_name, "a")
      f.write(f"{index}: {matched_sites[index]}\n")
  print("\n")


# Driver code
if __name__ == "__main__":
  site_lookup()
  site_log()