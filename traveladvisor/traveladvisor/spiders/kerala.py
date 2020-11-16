# -*- coding: utf-8 -*-
import scrapy


class KeralaSpider(scrapy.Spider):
    name = 'kerala'
    allowed_domains = ['www.tripadvisor.in']
    start_urls = ['https://www.tripadvisor.in/Tourism-g297631-Kerala-Vacations.html']

    def parse(self, response):
        places=response.xpath("//ul[@class='_2aDyanzw']/li")
        for place in places:
            tourist_places= place.xpath(".//div/a/div[2]/div/div/text()").get()
            
            link=place.xpath(".//div/a/@href").get()
            
            
            yield response.follow(url=link, callback=self.parse_place1,meta={'place':tourist_places})
    
    def parse_place1(self, response):
        tourist_places = response.request.meta['place']
        places1=response.xpath("//ul[@class='_2aDyanzw']/li")
        for place1 in places1:
         
            sub_places= place1.xpath(".//div/a/div[2]/div/div/text()").get()
            
            link=place1.xpath(".//div/a/@href").get()
            
            yield response.follow(url=link, callback=self.parse_place2,meta={'main_places':tourist_places,'sub_places':sub_places})
                           
                          
                  
                
                          
    def parse_place2(self, response):
        tourist_places = response.request.meta['main_places']
        sub_places = response.request.meta['sub_places']
        places2=response.xpath("//ul[@class='_2aDyanzw']/li")
        for place2 in places2:
         
            sub2_places= place2.xpath(".//div/a/div[2]/div/div/text()").get()
            
            link=place2.xpath(".//div/a/@href").get()
            
            yield response.follow(url=link, callback=self.parse_place3,meta={'main_places':tourist_places,'sub_places':sub_places,'sub2_places':sub2_places})
                           
    def parse_place3(self, response):
        tourist_places = response.request.meta['main_places']
        sub_places = response.request.meta['sub_places']
        sub2_places = response.request.meta['sub2_places']
        places3=response.xpath("//div[@class='Dq9MAugU T870kzTX LnVzGwUB']")
        for place3 in places3:
            
            name_id=place3.xpath(".//div/div/div[2]/span/a/text()").get()
         
            text= place3.xpath(".//div[2]/div/div//span[last()]/@class").get()
            if (text=='ui_bubble_rating bubble_50'):
                text1=5
            elif (text=='ui_bubble_rating bubble_40'):
                text1=4
            elif (text=='ui_bubble_rating bubble_30'):
                text1=3
            elif (text=='ui_bubble_rating bubble_20'):
                text1=2
            elif (text=='ui_bubble_rating bubble_10'):
                text1=1
            else:
                continue
            
            link=place3.xpath(".//div[2]/div[3]/div[2]/span/text()").get()
            
            yield{
                          'id':name_id,
                          'main_places':tourist_places,
                          'sub_places':sub_places,
                          'sub2_places':sub2_places,
                          'rating':text1,
                          'time':link

                
                          } 