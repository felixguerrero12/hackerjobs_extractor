import scrapy, time

class TinderSpider(scrapy.Spider):
  name = "Tinder"
  allowed_domains = ["https://jobs.lever.co"]
  start_urls = ["https://jobs.lever.co/matchgroup?department=Tinder&team=Information%20Security"]

  def parse(self, response):
      for resp in response.css('a.posting-title'):
        yield {
	    "jobs_title": resp.css('h5 *::text').extract_first(),
	    "jobs_location": resp.css('a.posting-title div span.sort-by-location *::text').extract(),
	    "jobs_url": resp.css('a.posting-title::attr(href)').extract(),
	    "company_logo": 'https://lever-client-logos.s3-us-west-2.amazonaws.com/108e7424-ff86-4d3b-a242-2d5af76f2c1c-1594763509617.png'
	}
	#if jobs_url:
	#   yield scrapy.Request(urljobs_url, self.scrape_job_post)

  def scrape_job_post(self, jobs_url):
      if next_page:
        yield scrapy.Request(
	  response.urljoin(next_page),
          callback=self.parse)
      return
