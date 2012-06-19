from scrapy import log
from scrapy.selector import HtmlXPathSelector

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from urlquery.items import UrlqueryItem

class UrlQuerySpider(CrawlSpider):
	name = 'urlquery'

	allowed_domains = ['urlquery.net']
	start_urls      = ['http://www.urlquery.net']


	rules = (
		Rule(
		SgmlLinkExtractor(restrict_xpaths='//table[@class="ui-widget ui-widget-content ui-corner-all"]/tbody/tr'), callback='parse_item'
		),
	)

	def parse_item(self, response):
		hxs   = HtmlXPathSelector(response)
		data = hxs.select('//table[@class="ui-widget ui-widget-content"]/tbody/tr/td[2]/text()').extract()

		i = UrlqueryItem()
		i['url'] = data[0].strip()
		i['ip']  = data[1].strip()
		i['asn'] = data[2].strip()
		i['location'] = data[3].strip()
		i['reportCreated'] = data[4].strip()
		i['alerts'] = data[5].strip()
		i['reputation'] = data[7].strip()
		i['userAgent'] = data[8].strip()
		i['adobeVersion'] = data[9].strip()
		i['javaVersion'] = data[10].strip()

		return item
