"""
Scrape LinkedIn Jobs to get a list of job posting URLs
"""
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

class LinkedInSpider(scrapy.Spider):
    """
    scrapy.Spider class for LinkedIn Jobs page
    """
    name = "linkedin"
    start_urls = list(map(get_start_url, range(0, 1000, 10)))

    def parse(self, response):
        """Parser for scrapy.Spider class"""
        filename = "post_urls.txt"
        with open(filename, "a", encoding="utf-8") as f:
            for href in response.css("a.base-card__full-link::attr(href)").getall():
                f.write(href + "\n")
