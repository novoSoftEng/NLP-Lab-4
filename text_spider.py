import scrapy

class TextSpider(scrapy.Spider):
    name = "text_spider"
    start_urls = [
       'https://www.aljazeera.net/politics',  # Replace with the URL you want to scrape
        "https://www.france24.com/ar/",
        "https://www.aa.com.tr/ar/"
        
    ]

    def parse(self, response):
        # Extract text from <p>, <h1>, <h2>, <h3>, <h4>, <h5>, <h6> tags
        paragraphs = response.css('p::text').getall()
        headers = response.css('h1::text, h2::text, h3::text, h4::text, h5::text, h6::text').getall()
        
        all_text = paragraphs + headers

        yield {
            'url': response.url,
            'text': ' '.join(all_text)
        }

        # Follow links to next pages
        for next_page in response.css('a::attr(href)').getall():
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

