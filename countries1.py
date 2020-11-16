import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries1'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # absolute_url = f"https://www.worldometers.info{link}"
            # absolute_url = response.urljoin(link)

            yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})

    def parse_country(self, response):
        name = response.request.meta['country_name']
        rows = response.xpath(
            "(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            med_age= row.xpath(".//td[9]/text()").getall()
            urban_pop= row.xpath(".//td[10]/text()").getall()
            world_share=row.xpath(".//td[11]/text()").getall()
            yield {
                'country_name': name,
                'year': year,
                'population': population,
                'Med_age': med_age,
                'Urban_pop': urban_pop,
                'World_share': world_share,

            }
