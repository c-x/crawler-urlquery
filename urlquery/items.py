# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class UrlqueryItem(Item):
	url  = Field()
	ip = Field()
	asn = Field()
	location = Field()
	reportCreated = Field()
	alerts = Field()
	reputation = Field()
	userAgent = Field()
	adobeVersion = Field()
	javaVersion = Field()
