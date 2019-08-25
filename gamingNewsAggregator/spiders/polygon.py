import scrapy

class polygon(scrapy.Spider):
    name = "polygon"
    start_urls = [
        'https://www.polygon.com/gaming',
    ]

    def parse(self, response):

        articles = response.xpath("//div[@class='c-compact-river']/div/div/div/h2")

        for art in articles:
            yield {
                'headline': art.css("a::text").get(),
                'link': art.css("a::attr(href)").get(),
                #'image': art.xpath("//a/div/img").css("img::attr(src)").get(), #base64 format
                #'author': art.xpath("//div/span").css("a::text").get(), #this is not working
            }
