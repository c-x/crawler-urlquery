# Scrapy settings for urlquery project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'urlquery'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['urlquery.spiders']
NEWSPIDER_MODULE = 'urlquery.spiders'

#USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13'

# MONGODB SETTINGS
MONGODB_SERVER = '127.0.0.1'
MONGODB_PORT   = 27017
MONGODB_DB     = 'scrapy'
#MONGODB_COLLECTION



ITEM_PIPELINES = [ 'urlquery.pipelines.WriteMongoDB' ]

