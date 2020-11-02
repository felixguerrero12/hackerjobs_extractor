import scrapy, time

class NetflixSpider(scrapy.Spider):
  name = "Netflix"
  allowed_domains = ["https://jobs.lever.co"]
  start_urls = ["https://jobs.lever.co/netflix/?department=Streaming&team=Information%20Security"]

  def parse(self, response):
      for resp in response.css('a.posting-title'):
        yield {
	    "jobs_title": resp.css('h5 *::text').extract_first(),
	    "jobs_location": resp.css('a.posting-title div span.sort-by-location *::text').extract(),
	    "jobs_url": resp.css('a.posting-title::attr(href)').extract(),
	    "company_logo": 'https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1442905953849.png'
	}
	#if jobs_url:
	#   yield scrapy.Request(urljobs_url, self.scrape_job_post)

  def scrape_job_post(self, jobs_url):
      if next_page:
        yield scrapy.Request(
	  response.urljoin(next_page),
          callback=self.parse)
      return
