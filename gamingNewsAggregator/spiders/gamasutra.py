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

        #for a in art:
            #a.css('a *::text').extract()

        # Links are not consistent... some contain https// and some do not?
        # Figure out way to append https// to those that don't start with it
        for art in articles:
            yield {
                #'headline': art.css('a::text').get() + art.xpath("//span[@class='story_title']/a/child::*//text()").get(),
                'headline': art.css('a *::text').extract(), #Must Concatenate all Elements Occurring Before '&nbsp'
                'link': art.css("a::attr(href)").get() #Link Works
                #'image': art.css("img::attr(src)").get(),
                #'image': art.xpath("//a/img[@class='thumbnail_left']").css("img::attr(src)").get()
            }
