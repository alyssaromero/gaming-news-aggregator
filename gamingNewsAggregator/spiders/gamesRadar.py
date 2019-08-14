import scrapy

class gamesRadar(scrapy.Spider):
    name = "gamesRadar"
    start_urls = [
        'https://www.gamesradar.com/news/',
    ]

    def parse(self, response):

        articles = response.xpath("//div[@class='listingResults news']/div/a[1]")

        #for some reason, all images are 'missing'... find correct images for display
        for art in articles:
            yield {
                'headline': art.css("h3::text").get(),
                'link': art.css("a::attr(href)").get()
                #'image': art.css("img::attr(src)").get()
            }
