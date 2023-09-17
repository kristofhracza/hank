from lib.setup import *

SITES,OPTIONS = make()
matched_sites = {}

def siteLookup(site, url):
  if OPTIONS.verbose:
    print(f"[*] {site} : {url}")
  try:
    req = requests.get(url,allow_redirects=True)
    if req.status_code == 200:
      matched_sites[site] = url
  except requests.exceptions.SSLError:
    print(f"[!] {site} SSL error")

def pretty():
  for index in matched_sites:
    print(f"{index}:\t{matched_sites[index]}")
    if OPTIONS.fileName:
      f = open(OPTIONS.fileName, "a")
      f.write(f"{index}: {matched_sites[index]}\n")
  print("\n")

def main():
  for s in SITES:
    siteLookup(s,SITES[s].format(OPTIONS.uname))


if __name__ == "__main__":
  main()
  pretty()