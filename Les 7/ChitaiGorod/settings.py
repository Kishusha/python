BOT_NAME = 'ChitaiGorod'

SPIDER_MODULES = ['ChitaiGorod.spiders']
NEWSPIDER_MODULE = 'ChitaiGorod.spiders'


USER_AGENT = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.94')

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 8

DOWNLOAD_DELAY = 3
CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_REQUESTS_PER_IP = 8

COOKIES_ENABLED = False

TELNETCONSOLE_ENABLED = False

RETRY_HTTP_CODES = [429]

ITEM_PIPELINES = {
    'ChitaiGorod.pipelines.ChitaiGorodImagePipeline': 100,
    'ChitaiGorod.pipelines.MongoPipeline': 300,
}

IMAGES_STORE = '/tmp/images'

