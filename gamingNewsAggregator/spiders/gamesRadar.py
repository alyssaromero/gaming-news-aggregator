import scrapy

class gamesRadar(scrapy.Spider):
    name = "gamesRadar"
    start_urls = [
        'https://www.gamesradar.com/news/',
    ]

    def parse(self, response):

        articles = response.xpath("//div[@class='listingResults news']/div/a[1]")
        #articles = response.xpath("//div[@class='listingResults news']/div/a[1]/article/div/header/p/span[@class='by-author']/span")

        for art in articles:
            yield {
                'headline': art.css("h3::text").get(),
                'link': art.css("a::attr(href)").get(),
                'image': art.css("img::attr(data-src)").get(),
                'author': art.xpath("//article/div/header/p/span[@class='by-author']/span").css("span::text").get()
            }
