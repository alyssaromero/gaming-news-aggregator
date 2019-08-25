import scrapy

### THIS CRAWLER IS COMPLETE ###
class gameInformer(scrapy.Spider):
    name = "gameInformer"
    start_urls = [
        "https://www.gameinformer.com/news",
    ]

    def parse(self, response):

        articles = response.xpath("//div[@class='view-content']/div/div")

        for art in articles:
            yield {
                'headline': art.css("span::text").get(),
                'link': "https://www.gameinformer.com" + art.css("a::attr(href)").get(),
                'image': art.css("img::attr(src)").get(),
                #'author': art.xpath("//article/div/div/div").css("a::text").get() #this is not working
            }
