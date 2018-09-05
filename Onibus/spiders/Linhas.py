# -*- coding: utf-8 -*-
import scrapy

class LinhasSpider(scrapy.Spider):

    name = 'Linhas'    
    start_urls = ['http://www.ctaonline.com.br/index.php/linhas.html']

    def parse_conteudo(self, response):

        ##pagina toda
        itinerarios = response.xpath('//*[@id="component"]/div/article/section[2]/div/div/div/div/div/div/div/div/div')
        ##titulo
        title = response.xpath('//*[@id="component"]/div/article/header/h1/a/text()').extract_first()

        ##Rotas
        for iot in itinerarios:
            rota = iot.xpath('//div[contains(@class, "wpb_wrapper")]/p')
            for iott in rota:
                teste1 = iott.xpath('./text()').extract_first()
                if teste1 != None:
                    print(teste1)

        ##Organização dos Horários
        for p in itinerarios:
            var = p.xpath('.//p')
            for pp in var:
                strong = pp.xpath('.//span/text()').extract()
                print(strong)

        ##Recuperação de Horários
        for p in itinerarios:
            var = p.xpath('.//table')
            for pp in var:
                var1 = pp.xpath('.//tr')
                for ppp in var1:
                    var2 = ppp.xpath('.//td/span/text()').extract()
                    print(var2)

        # for iot in itinerarios:
        #     teste = iot.xpath('//div[contains(@class, "wpb_wrapper")]/p[1]/text()').extract_first()


   
    def parse_links(self, response):
        empresa = response.xpath('//div[contains(@class, "grid3 column first last ex-odd multi-module-column sidebar-a")]')
        for cat in empresa:
            teste = cat.xpath('//div[contains(@class, "block module")]/div[contains(@class, "content")]/ul/li/a')            
            for li in teste:
                link = li.xpath('./@href').extract_first()
                self.log('Category: %s' % link)
            # yield scrapy.Request(
            #     # url = 'http://www.ctaonline.com.br%s' % link,               
            #     callback=self.parse_category
            # )

       
