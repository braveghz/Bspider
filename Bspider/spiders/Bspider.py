import scrapy


class Bspider(scrapy.Spider):
    name = "Bspider"
    start_url = ["https://www.zhihu.com/topic/19552207/hot"]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
