"""
Scrape LinkedIn job posts to get job descriptions
"""
import json
import scrapy

def get_post_urls():
    """
    Read post_urls.txt to get a list of URLs to scrape
    """
    filename = "post_urls.txt"
    with open(filename, "r", encoding="utf-8") as f:
        return list(map(str.strip, f.readlines()))

def save_json(input_list):
    """
    Save a given input list into orgs.json
    """
    filename = "orgs.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(input_list, f, indent=4)

def process_response(response):
    """
    Returns a LinkedIn job webpage's description from a given page response
    """
    tags = response.css("a.topcard__org-name-link ::text").getall()
    return "\n".join(filter(bool, map(str.strip, tags))).strip()

class OrgSpider(scrapy.Spider):
    """
    scrapy.Spider class for a LinkedIn job post page Organization
    """
    name = "orgs"
    start_urls = get_post_urls()
    orgs = []

    def parse(self, response):
        """Parser for scrapy.Spider class"""
        string = process_response(response)
        self.orgs.append(string)

    def closed(self, _):
        """Executes at end of crawl"""
        save_json(self.orgs)
