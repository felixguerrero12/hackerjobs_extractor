import scrapy, time

class HashiCorpSpider(scrapy.Spider):
  name = "Auth0"
  allowed_domains = ["https://jobs.lever.co"]
  start_urls = ["https://jobs.lever.co/auth0?team=Security"]

  def parse(self, response):
      for resp in response.css('a.posting-title'):
        yield {
	    "jobs_title": resp.css('h5 *::text').extract_first(),
	    "jobs_location": resp.css('a.posting-title div span.sort-by-location *::text').extract(),
	    "jobs_url": resp.css('a.posting-title::attr(href)').extract(),
	    "company_logo": 'https://lever-client-logos.s3.amazonaws.com/Auth0.png'
	}
	#if jobs_url:
	#   yield scrapy.Request(urljobs_url, self.scrape_job_post)

  def scrape_job_post(self, jobs_url):
      if next_page:
        yield scrapy.Request(
	  response.urljoin(next_page),
          callback=self.parse)
      return
