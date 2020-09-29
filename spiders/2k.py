import scrapy, time

class TwoKSpider(scrapy.Spider):
  name = "2k"
  allowed_domains = ["boards.greenhouse.io"]
  start_urls = ["https://boards.greenhouse.io/2k/"]

  def parse(self, response):
      for resp in response.css('div.opening[department_id="4013194003,4013207003"]'):
        yield {
	    "jobs_title": resp.css('a *::text').extract_first(default=''),
	    "jobs_location": resp.css('span.location *::text').extract_first(default=''),
	    "jobs_url": response.urljoin(resp.css('a::attr(href)').extract_first(default='')),
	    "company_img_url": response.css('img::attr(src)').extract_first()
	}
	#if jobs_url:
	#   yield scrapy.Request(urljobs_url, self.scrape_job_post)

  def scrape_job_post(self, jobs_url):
      if next_page:
        yield scrapy.Request(
	  response.urljoin(next_page),
          callback=self.parse)
      return
