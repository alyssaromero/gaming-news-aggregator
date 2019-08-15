import scrapy

### THIS CRAWLER IS COMPLETE ###
class gameInformer(scrapy.Spider):
    name = "gameInformer"
    start_urls = [
        "https://www.gameinformer.com/news",
    ]

    def parse(self, response):

        articles = a

        for art in articles:
            yield {
                'headline': art.css("span::text").get(),
                'link': "https://www.gameinformer.com" + art.xpath("//div[@class='promo-img-thumb']").css("a::attr(href)").get(),
                'image': art.css("img::attr(src)").get()
            }
