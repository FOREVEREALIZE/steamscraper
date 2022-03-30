import scrapy


class SteamSpider(scrapy.Spider):
    name = 'steamspider'
    start_urls = ['https://store.steampowered.com/search?sort_by=Released_DESC']

    def parse(self, response):
        for game in response.css('#search_result_row'):
            yield { 'link': game.attrib['href'] }

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)