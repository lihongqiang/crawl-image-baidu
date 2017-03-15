import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
from scrapy.exceptions import DropItem
import functools
import hashlib
import six
from scrapy.utils.python import to_bytes
from scrapy.http import Request
import io
import urllib

class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        url = item['image_urls'][0]
        request = scrapy.Request(url)
        request.meta['word'] = item['image_label']
        # print item['image_label']
        yield request

    def item_completed(self, results, item, info):
        for ok, x in results:
            if ok:
                image_path = x['path']
                item['image_paths'] = image_path

                f = io.open("image_infos.csv",  'a', encoding = 'utf-8')
                f.write(item['image_label'] + "," + item['image_paths'] + "," + item['image_urls'][0] + "\n")
                f.close()

                return item

    def file_path(self, request, response=None, info=None):
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('ImagesPipeline.image_key(url) and file_key(url) methods are deprecated, '
                          'please use file_path(request, response=None, info=None) instead',
                          category=ScrapyDeprecationWarning, stacklevel=1)

        if not isinstance(request, Request):
            _warn()
            url = request
        else:
            url = request.url
        image_guid = hashlib.sha1(to_bytes(url)).hexdigest()  # change to request.url after deprecation
        word = request.meta['word']
        # word = urllib.unquote(word).decode('utf-8')
        return word + '/%s.jpg' % (image_guid)



# class FilterWordsPipeline(object):
#     """A pipeline for filtering out items which contain certain words in their
#     description"""

    # put all words in lowercase
    # words_to_filter = ['politics', 'religion']


    # def process_item(self, item, spider):
    #     return item
