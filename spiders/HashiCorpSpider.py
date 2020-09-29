import scrapy, time

class HashiCorpSpider(scrapy.Spider):
  name = "HashiCorp"
  allowed_domains = ["www.hashicorp.com"]
  start_urls = ["https://www.hashicorp.com/jobs/security"]

  def parse(self, response):
      for resp in response.css('li.item a'):
        yield {
	    "jobs_title": resp.css('span.g-type-display-6.title *::text').extract_first(default=''),
	    "jobs_location": resp.css('p.g-type-label.location *::text').extract_first(default=''),
	    "jobs_url": response.urljoin(resp.css('a::attr(href)').extract_first(default=''))
	}
	#if jobs_url:
	#   yield scrapy.Request(urljobs_url, self.scrape_job_post)

  def scrape_job_post(self, jobs_url):
      if next_page:
        yield scrapy.Request(
	  response.urljoin(next_page),
          callback=self.parse)
      return
