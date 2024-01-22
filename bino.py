from lib.setup import *
from random import choice

# Main variables
SITES,OPTIONS = make()
matched_sites = {}


# Query sites
def site_lookup():
  for site in SITES:
    url = SITES[site].format(OPTIONS.user_name)
    if OPTIONS.verbose:
      print(f"[*] {site}:\t{url}")
    try:
      req = requests.get(url, headers={"User-Agent":choice(UA)})
      if req.status_code == 200:
        if site not in matched_sites.values():
          matched_sites[site] = url
    except requests.exceptions.SSLError:
      print(f"[!] {site} is unreachable, might be blocked")
    

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