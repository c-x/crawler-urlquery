# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy import log

from urlquery.items import UrlqueryItem

class WriteMongoDB(object):

	def __init__(self):
		cnx = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
		self.db = cnx[settings['MONGODB_DB']]
		#self.col= self.db[settings['MONGODB_COLLECTION']]



	def process_item(self, item, spider):

		col = None
		if( isinstance(item, UrlqueryItem) ):
			col = self.db[ 'urlquery' ]
			n = col.find( {'url' : item['url']} ).count()

			if( n > 0 ):
				log.msg("MongoDB Pipeline : Record already exist (%s)" % (item['url']))
				col = None
		else:
			log.msg("MongoDB Pipeline : Unrecognized item" , level=log.DEBUG, spider=spider	)

		if( col ):
			col.insert(dict(item))
	# eof __init__


