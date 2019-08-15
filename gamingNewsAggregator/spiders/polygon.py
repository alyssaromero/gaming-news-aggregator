import scrapy

class polygon(scrapy.Spider):
    name = "polygon"
    start_urls = [
        'https://www.polygon.com/gaming',
    ]


    # SOME HEADLINES HAVE UNICODE IN THEM... NEED TO CONVERT WHEN SAVING TO DB #
    def parse(self, response):


        articles = response.xpath("//div[@class='c-compact-river']/div/div") #/div/h2")
        #articles = response.xpath("//div[@class='c-compact-river']/div/div/div/div/span")

        for art in articles:
            yield {
                'headline': art.xpath("//div/h2").css("a::text").get(),
                'link': art.xpath("//div/h2").css("a::attr(href)").get(),
                'image': art.xpath("//a/div/img").css("img::attr(src)").get(),
                'author': art.xpath("//div/span").css("a::text").get(),
            }
