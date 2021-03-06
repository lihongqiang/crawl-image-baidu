# Scrapy settings for dirbot project
#!/usr/bin/python
# -*- coding: utf-8 -*-

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.MyImage'

# ITEM_PIPELINES = {'dirbot.pipelines.FilterWordsPipeline': 1}
ITEM_PIPELINES = {'dirbot.pipelines.MyImagesPipeline': 1}

DOWNLOADER_MIDDLEWARES = {
        'scrapy.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'dirbot.rotate_useragent.RotateUserAgentMiddleware': 100,
        # 'dirbot.rotate_middlewares.ProxyMiddleware': 200,
    }

IMAGES_STORE = 'D:/lhq/openimages/profession-search-360/'
IMAGES_LABEL = ''

IMAGES_EXPIRES = 90

# IMAGES_THUMBS = {
#     'small': (400, 400),
#     'big': (800, 800),
# }

IMAGES_MIN_HEIGHT = 300
IMAGES_MIN_WIDTH = 300

# IMAGES_URLS_FIELD = 'field_name_for_your_images_urls'
# IMAGES_RESULT_FIELD = 'field_name_for_your_processed_images'

# forbid cookie
COOKIES_ENABLED = False
# forbid retry
RETRY_ENABLED = True
# set timeout
DOWNLOAD_TIMEOUT = 60

# close redirect
REDIRECT_ENABLED = True

# Ajax crawl
AJAXCRAWL_ENABLED = True

# set log level
LOG_LEVEL = 'INFO'

# concurrence
CONCURRENT_REQUESTS = 60

# delay for address
DOWNLOAD_DELAY = 2   # 1 s of delay
CONCURRENT_REQUESTS_PER_DOMAIN = 2

# delay for ip
# CONCURRENT_REQUESTS_PER_IP = 8

# auto delay

AUTOTHROTTLE_ENABLED = True

AUTOTHROTTLE_START_DELAY = 2

AUTOTHROTTLE_MAX_DELAY = 10

AUTOTHROTTLE_DEBUG = True

# agent
USER_AGENTS = [
    # "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    # "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    # "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    # "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    # "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
	# "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
	# "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
	# "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
	# "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
	# "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
	# "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
	# "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
	# "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
	# "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	# "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
	# "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

# proxy
PROXIES = [
    # {'ip_port': '106.46.136.119:808', 'user_pass': ''},
    # {'ip_port': '183.157.184.163:80', 'user_pass': ''},
    # {'ip_port': '110.73.149.190:8123', 'user_pass': ''},
    # {'ip_port': '183.32.88.158:808', 'user_pass': ''},
    # {'ip_port': '111.72.126.14:808', 'user_pass': ''},
    # {'ip_port': '183.140.99.29:80', 'user_pass': ''},
    # {'ip_port': '124.88.67.63:80', 'user_pass': ''},
    # {'ip_port': '119.5.1.51:808', 'user_pass': ''},
    # {'ip_port': '61.143.136.114:8998', 'user_pass': ''},
    # {'ip_port': '58.23.122.79:8118', 'user_pass': ''},
    # {'ip_port': '101.53.101.172:9999', 'user_pass': ''},
    # {'ip_port': '124.88.67.52:843', 'user_pass': ''},
    # {'ip_port': '124.88.67.21:843', 'user_pass': ''},
    # {'ip_port': '124.88.67.10:80', 'user_pass': ''},
]