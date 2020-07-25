import scrapy


class AdminSpider(scrapy.Spider):
    name ="admins"
    start_urls = [
        'http://103.27.36.114/sipandu2/ID_barang_perbandingan.php'
    ]

    def parse(self, response):
        title = response.xpath("/html/body/div[1]/div[2]/div[2]/table[2]/tr[20]/td/text()").getall()
        yield {
            'titletext': title
        }