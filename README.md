# Scraper
 This scraper is used to extract jobs from different job boards.

# Use of this Scraper:
```
scrapy runspider ClearSpider.py -o clear.csv -t csv

Run all Spiders:
ls spiders/*.py | grep -v "__init__.py" |xargs -n 1 scrapy runspider -o result.json -t json
```
