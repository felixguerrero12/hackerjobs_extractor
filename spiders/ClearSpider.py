import scrapy, time

class ClearSpider(scrapy.Spider):
  name = "clear"
  allowed_domains = ["boards.greenhouse.io"]
  start_urls = ["https://boards.greenhouse.io/clear/"]


#  def parse(self, response):
#    data = {}
#    for jobs in response.css('div.opening[department_id="5705,57838"]').extract():
#      data['jobs_title'] = response.css('div.opening[department_id="5705,57838"] a *::text').extract_first()
#      data['jobs_location'] = response.css('div.opening[department_id="5705,57838"] span.location *::text').extract_first()
#      data['jobs_url'] = response.css('div.opening[department_id="5705,57838"] a::attr(href)').extract_first()
#      for href in response.css('div.opening[department_id="5705,57838"] a::attr(href)').extract_first():
#        data['jobs_url'] = response.urljoin(href)
#    yield data

  def parse(self, response):
      for resp in response.css('div.opening[department_id="5705,57838"]'):
        yield {
	    "jobs_title": resp.css('a *::text').extract_first(default=''),
	    "jobs_location": resp.css('span.location *::text').extract_first(default=''),
	    "jobs_url": response.urljoin(resp.css('a::attr(href)').extract_first(default=''))
	}
