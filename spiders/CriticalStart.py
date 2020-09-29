import scrapy, time

class CriticalStartSpider(scrapy.Spider):
  name = "CriticalStart"
  allowed_domains = ["https://jobs.lever.co"]
  start_urls = ["https://jobs.lever.co/criticalstart?department=&team=Professional%20Services"]

  def parse(self, response):
      for resp in response.css('a.posting-title'):
        yield {
	    "jobs_title": resp.css('h5 *::text').extract_first(),
	    "jobs_location": resp.css('a.posting-title div span.sort-by-location *::text').extract(),
	    "jobs_url": resp.css('a.posting-title::attr(href)').extract(),
	    "company_logo": 'https://lever-client-logos.s3-us-west-2.amazonaws.com/de78f122-c406-460e-8030-db9dd161b651-1592518620004.png'
	}
	#if jobs_url:
	#   yield scrapy.Request(urljobs_url, self.scrape_job_post)

  def scrape_job_post(self, jobs_url):
      if next_page:
        yield scrapy.Request(
	  response.urljoin(next_page),
          callback=self.parse)
      return
