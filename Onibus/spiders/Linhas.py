# -*- coding: utf-8 -*-
import scrapy

class LinhasSpider(scrapy.Spider):

    name = 'Linhas'
    allowed_domains = ['https://www.ctaonline.com.br/index.php/linhas.html']
    start_urls = ['https://www.ctaonline.com.br/index.php/linhas.html']

    def parse(self, response):
        """ Main function that parses downloaded pages """
        # Print what the spider is doing
        print(response.url)
        # Get all the <a> tags
        a_selectors = response.xpath("//a")
        # Loop on each tag
        for selector in a_selectors:
            # Extract the link text
            text = selector.xpath("text()").extract_first()
            # Extract the link href
            link = selector.xpath("@href").extract_first()
            # Create a new Request object
            request = response.follow(link, callback=self.parse)
            # Return it thanks to a generator
            yield request

   
    # def parse(self, response):
    #     empresa = response.xpath('//div[contains(@class, "grid3 column first last ex-odd multi-module-column sidebar-a")]').extract_first()
    #     for cat in empresa:
    #          = cat.xpath('//div[contains(@class, "block module")]/div[contains(@class, "content")]/ul/li/a/')

    #         self.log('Category: %s' % cat_url)
    #         yield scrapy.Request(
    #             url = 'http://www.ctaonline.com.br%s' % cat_url,               
    #             callback=self.parse_category
    #         )

       
    # def parse_category(self, response):
    #     self.log(response.xpath("//title/text()").extract_first())