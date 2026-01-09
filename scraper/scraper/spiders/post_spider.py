"""
Scrape LinkedIn job posts to get job descriptions
"""
import json
import scrapy

def read_json():
    """
    Read post_urls.json to get a list of URLs to scrape
    """
    filename = "post_urls.json"
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(input_list, filename):
    """
    Save a given input list into a file with a given filename
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(input_list, f, indent=4)

def process_response(response):
    """
    Returns a LinkedIn job webpage's description and organization from a given page response
    """
    def get_jd():
        """Get job description from LinkedIn job webpage from a given response"""
        tags = response.css("section.show-more-less-html ::text").getall()
        return "\n".join(filter(bool, map(str.strip, tags))).strip()
    def get_org():
        """Get hiring organization from LinkedIn job webpage from a given response"""
        tags = response.css("a.topcard__org-name-link ::text").getall()
        return "\n".join(filter(bool, map(str.strip, tags))).strip()
    return get_jd(), get_org()

class PostSpider(scrapy.Spider):
    """
    scrapy.Spider class for a LinkedIn job post page
    """
    name = "posts"
    start_urls = read_json()
    jds = []
    orgs = []

    def parse(self, response):
        """Parser for scrapy.Spider class"""
        jd, org = process_response(response)
        self.jds.append(jd)
        self.orgs.append(org)

    def closed(self, _):
        """Executes at end of crawl"""
        save_json(self.jds, "job_descriptions.json")
        save_json(self.orgs, "orgs.json")
