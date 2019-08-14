import scrapy

class gamasutra(scrapy.Spider):
    name = "gamasutra"
    start_urls = [
        'https://www.gamasutra.com/updates/',
    ]

    def parse(self, response):

        articles = response.xpath("//div[@class='content_box_middle']/div[@class='feed_item']")
        #articles = response.xpath("//div[@class='content_box_middle']/div[@class='feed_item']/span/span")
        #image = response.xpath("//div[@class='content_box_middle']/div[@class='feed_item']/a")

        #for some reason, xpaths are not grabbing italized titles... fix this
        for art in articles:
            yield {
                'headline': art.css('a::text').get(),
                #'headline': art.xpath("//div[@class='feed_item']/span/span[@class='story_title']").css("a::text").get(),
                'link': art.css("a::attr(href)").get()
                #'link': art.xpath("//div[@class='feed_item']/span/span[@class='story_title']").css("a::attr(href)").get(),
                #'image': art.css("img::attr(src)").get(),
                #'image': art.xpath("//a/img[@class='thumbnail_left']").css("img::attr(src)").get()
            }
