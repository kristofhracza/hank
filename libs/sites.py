"""

URL crawler, look at different social sites and checks whether the username is present

"""
from libs.resources import *

class Binoculars():
    def __init__(self,OPTIONS):
        self.options = OPTIONS
        self.sites = {}
        self.matched_sites = {}

    # Load site URLs from the JSON file
    def read_sites(self):
        with open("sites.json") as config:
            self.sites = json.load(config)

    # Look up sites
    def site_lookup(self):
        for site in self.sites:
            url = self.sites[site].format(self.options.user_name)
            try:
                req = requests.get(url, headers={"User-Agent":random.choice(USER_AGENTS)},allow_redirects=False)
                if req.status_code == 200:
                    self.matched_sites[site] = url
                    print(f"[*] {site}: {url}")
                else:
                    print(f"[-] {site}: {url}")
            except KeyboardInterrupt:
                print("[!] Aboriting site scan...")
                break
            except:
                print(f"[-] {site}: {url}")

    # Log sites that have been found
    def site_log(self):
        if len(self.matched_sites) > 0:
            print("\n============= Active links =============")
            for index in self.matched_sites:
                print(f"{index}:\t{self.matched_sites[index]}")

    # Run all functions
    def run(self):
        print(site_lookup_banner)
        self.read_sites()
        self.site_lookup()
        self.site_log()
