import scrapy

class polygon(scrapy.Spider):
    name = "polygon"
    start_urls = [
        'https://www.polygon.com/gaming',
    ]


    # SOME HEADLINES HAVE UNICODE IN THEM... NEED TO CONVERT WHEN SAVING TO DB #
    def parse(self, response):

        articles = response.xpath("//div[@class='c-compact-river']/div/div/div/h2")

        for art in articles:
            yield {
                'headline': art.css("a::text").get(),
                'link': art.css("a::attr(href)").get(),
            }
