import scrapy, time

# Still need to filter to only Trust and Security
# Requires the removal of /n that are empty

class MozillaSpider(scrapy.Spider):
  name = "Mozilla"
  allowed_domains = ["careers.mozilla.org"]
  start_urls = ["https://careers.mozilla.org/listings/"]

  def parse(self, response):
      for resp in response.css('body.listings-page div.mzp-l-content.mzp-t-mozilla main:nth-child(1) section.mzp-l-content table.listings-positions tr'):
        yield {
	    "jobs_title": resp.css('td.title *::text').extract_first(default=''),
	    "jobs_location": resp.css('td.location *::text').extract_first(default=''),
	    "jobs_url": response.urljoin(resp.css('td.title a::attr(href)').extract_first(default='')),
	    "company_img_url": 'https://careers.mozilla.org/static/img/favicon.d4f1f46b91f4.ico',
	    "team": resp.css('td.name *::text').extract_first(default='')
	}
	#if jobs_url:
	#   yield scrapy.Request(urljobs_url, self.scrape_job_post)

  def scrape_job_post(self, jobs_url):
      if next_page:
        yield scrapy.Request(
	  response.urljoin(next_page),
          callback=self.parse)
      return
