from scrapy.item import Item, Field


class MyImage(Item):

    image_urls = Field()
    images = Field()
    image_paths = Field()
    image_label = Field()
