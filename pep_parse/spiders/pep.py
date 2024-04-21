import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import MAIN_URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [MAIN_URL]
    start_urls = [f'https://{url}/' for url in allowed_domains]

    def parse(self, response):
        pep_links = response.css(
            '#numerical-index tbody a[href^="pep-"]::attr(href)'
        )
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        data = dict(
            number=title.split(' ')[1],
            name=title.split(' – ')[1],
            status=response.css('abbr::text').get(),
        )
        yield PepParseItem(data)
