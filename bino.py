from lib.setup import *

# Main variables
SITES,OPTIONS = make()
matched_sites = {}


# Query sites
def siteLookup(site, url):
  if OPTIONS.verbose:
    print(f"[*] {site} :\t{url}")
  try:
    req = requests.get(url, headers={"User-Agent":random.choice(UA)})
    if req.status_code == 200:
      if site not in matched_sites.values():
        matched_sites[site] = url
  except requests.exceptions.SSLError:
    print(f"[!] {site} is unreachable, might be blocked")


# Log output
def pretty():
  for index in matched_sites:
    print(f"{index}:\t{matched_sites[index]}")
    if OPTIONS.fileName:
      f = open(OPTIONS.fileName, "a")
      f.write(f"{index}: {matched_sites[index]}\n")
  print("\n")


# Main  loop
def main():
  for s in SITES:
    siteLookup(s,SITES[s].format(OPTIONS.uname))


# Driver code
if __name__ == "__main__":
  main()
  pretty()