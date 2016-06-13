#from scrapy.spiders import Spider
#from scrapy.selector import Selector
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from webcrawler.items import Website


class ClubCrawlerSpider(CrawlSpider):
	name = "club"
	allowed_domains = ["stackoverflow.com"]
	start_urls = [
		"http://www.stackoverflow.com/questions?pagesize=50&sort=newest",
#		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]
	rules = (
		Rule(LinkExtractor(allow=r'questions\?page=[0-2]&sort=newest'), callback='parse_item', follow=True),
		# Follow any item link and call parse_item.
#        Rule(LinkExtractor(allow=('item.*', )), callback='parse_item'),
	)
	# normally set in settings.py
	custom_settings = {
		'BOT_NAME': 'club-scraper',
		'DEPTH_LIMIT': 7,
		'DOWNLOAD_DELAY': 3
	}


	# def parse(self, response):
	def parse_item(self, response):
		questions = response.xpath('//div[@class="summary"]/h3')

		for site in questions:
			item = Website()
#			item['name'] = site.xpath('a/text()').extract()
			item['url'] = site.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
			item['desc'] = site.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
#			items.append(item)

			print item

			yield item

		# s = Selector(response)
  #       next_link = s.xpath('//span[@class="nextprev"]//a/@href').extract()[0]
  #       if len(next_link):
  #           yield self.make_requests_from_url(next_link)
  #       posts = Selector(response).xpath('//div[@id="siteTable"]/div[@onclick="click_thing(this)"]')
  #       for post in posts:
  #           i = TextPostItem()
  #           i['title'] = post.xpath('div[2]/p[1]/a/text()').extract()[0]
  #           i['url'] = post.xpath('div[2]/ul/li[1]/a/@href').extract()[0]
  #           i['submitted'] = post.xpath('div[2]/p[2]/time/@title').extract()[0]
  #           yield i

#		return items
