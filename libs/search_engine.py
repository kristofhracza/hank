"""

Search engine crawler, returns links that are most likely related to the user

"""
from libs.resources import *

# Class the represents the search engine itself and does all the querying
class Search_Engine():
    def __init__(self,OPTIONS):
        self.options = OPTIONS
        self.bing = "https://www.bing.com/search?q={}"
        self.google = "https://www.google.com/search?q={}"
        self.url_pattern = re.compile(r"https?://\S+")
        self.greedy = 5 if self.options.count == None else int(self.options.count)
        self.bing_elements = []
        self.google_elements = []


    # Crawl and parse data
    def main_process(self):
        # GET data
        google_req = requests.get(self.google.format(self.options.real_name),headers={"User-Agent":random.choice(USER_AGENTS)})
        bing_req = requests.get(self.bing.format(self.options.real_name),headers={"User-Agent":random.choice(USER_AGENTS)})

        # Parse HTML
        g_soup = BeautifulSoup(google_req.text,"html.parser")
        d_soup = BeautifulSoup(bing_req.text,"html.parser")

        # Process optimal data into dictionaries and lists
        for name in self.options.real_name.split():
            self.bing_elements.append(d_soup.find_all("a",href=re.compile(re.escape(name), re.IGNORECASE)))
            self.google_elements.append(g_soup.find_all("a",href=re.compile(re.escape(name), re.IGNORECASE)))
        # Now do this for more accurate results
        self.bing_elements.append(d_soup.find_all("a",href=re.compile(re.escape(self.options.real_name), re.IGNORECASE)))
        self.google_elements.append(g_soup.find_all("a",href=re.compile(re.escape(self.options.real_name), re.IGNORECASE)))
        


    # Process data that has been collected and add it to a collective
    def process_collected_data(self):
        href_arr = []
        for g_elem, b_elem in zip(self.google_elements,self.bing_elements):
            g_elem = list(set(g_elem))
            b_elem = list(set(b_elem))
            for g,b in zip(g_elem,b_elem):
                match_g = self.url_pattern.search(g["href"])
                match_b = self.url_pattern.search(b["href"])
                if match_g:
                    href_arr.append(g["href"])
                if match_b:
                    href_arr.append(b["href"])
                    
        return list(set(href_arr))

    # Run the class a few times to get as many links as possible
    def gather_more(self):
        greedy_arr = []
        count = 0
        for i in range(self.greedy):
            count += 1
            print(f"[*] Gathering links: [{'#'*count}{' '*(self.greedy-count)}]", end='\r')
            self.main_process()
            for link in self.process_collected_data():
                greedy_arr.append(link)
        return list(set(greedy_arr))

    # Clean all data and finalise the tasks
    def clean_and_run(self):
        print(search_engine_banner)
        arr = self.gather_more()
        trash = []
        for link in arr:
            if ("google" in link) or ("bing" in link):
                trash.append(link)
        for link in trash:
            arr.remove(link)

        print("\n\n============= Links found =============")
        for i in arr:
            print(i)
        return arr
