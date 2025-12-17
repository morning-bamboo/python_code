import scrapy


class CarhomeSpider(scrapy.Spider):
    name = "carhome"
    allowed_domains = ["www.autohome.com.cn/price/brandid_15"]
    start_urls = ["https://www.autohome.com.cn/price/brandid_15"]

    def parse(self, response):
        print("===================")
        print("===================")
        name_list = response.xpath('//div[@class="tw-mb-2 tw-flex tw-flex-wrap tw-items-center"]/a/text()')
        # print(name_list) # result is a Selector list - using for to loop
        price_list = response.xpath('//a[@class="tw-text-[16px] tw-font-[500] !tw-text-[#f60]"]/text()')
        rating_list = response.xpath('//strong[@class="tw-text-xs tw-font-[500]"]/text()')
        for i in range(len(name_list)):
            name = name_list[i]
            price = price_list[i]
            rating = rating_list[i]
            print(name, price, rating)

