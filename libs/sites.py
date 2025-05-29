# URL crawler, look at different social sites and checks whether the username is present

from libs.resources import *

class Binoculars():
    """
    Look up username on sites
    """
    def __init__(self,OPTIONS):
        self.options = OPTIONS
        self.sites = {}
        self.matched_sites = {}

    def read_sites(self):
        """
        Load site URLs from the JSON file
        """
        with open("sites.json") as config:
            self.sites = json.load(config)

    def site_lookup(self):
        """
        Look up sites
        """
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

    def site_log(self):
        """
        Log sites that have been found
        """
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
