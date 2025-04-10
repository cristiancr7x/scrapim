import scrapy

class SqliUrlCollectorSpider(scrapy.Spider):
    name = "sqli_url_collector"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com/search?q=test"]

    def parse(self, response):
        urls = response.css("a::attr(href)").getall()
        for url in urls:
            if "?" in url and "=" in url:
                yield {"sqli_candidate_url": response.urljoin(url)}
