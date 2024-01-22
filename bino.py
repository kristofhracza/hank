from lib.setup import *

SITES,OPTIONS = make()
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}
matched_sites = {}

def siteLookup(site, url):
  if OPTIONS.verbose:
    print(f"[*] {site} : {url}")
  try:
    req = requests.get(url, headers=HEADERS)
    if req.status_code == 200:
      if site not in matched_sites.values():
        matched_sites[site] = url
  except requests.exceptions.SSLError:
    print(f"[!] {site} is unreachable, might be blocked")

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