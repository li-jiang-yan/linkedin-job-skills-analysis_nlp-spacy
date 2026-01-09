"""
Scrape LinkedIn Jobs to get a list of job posting URLs
"""
import json
import scrapy

KEYWORDS = "Computer%20Science"
LOCATION = "Singapore"

def get_start_url(start):
    """
    Return a URL consisting of LinkedIn job posts with a given start field
    """
    result = ("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
              f"?keywords={KEYWORDS}"
              f"&location={LOCATION}"
              f"&start={start}")
    return result

def save_json(input_list):
    """
    Save a given input list into orgs.json
    """
    filename = "post_urls.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(input_list, f, indent=4)

class LinkedInSpider(scrapy.Spider):
    """
    scrapy.Spider class for LinkedIn Jobs page
    """
    name = "linkedin"
    start_urls = list(map(get_start_url, range(0, 1000, 10)))
    post_urls = []

    def parse(self, response):
        """Parser for scrapy.Spider class"""
        self.post_urls += list(response.css("a.base-card__full-link::attr(href)").getall())

    def closed(self, _):
        """Executes at end of crawl"""
        save_json(self.post_urls)
