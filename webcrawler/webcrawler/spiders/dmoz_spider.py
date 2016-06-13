from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector


class DmozSpider(BaseSpider):
	name = "dmoz"
	allowed_domains = ["dmoz.org"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		sites = hxs.xpath('//ul/li')
		for site in sites:
			title = site.xpath('a/text()').extract()
			link = site.xpath('a/@href').extract()
			desc = site.xpath('text()').extract()
			print title, link, desc
#		filename = response.url.split("/")[-2]
#		open(filename, 'wb').write(response.body)
