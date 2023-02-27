# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Bigdata2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    g_url = scrapy.Field()
    g_reviewer_name = scrapy.Field()
    g_comment_date = scrapy.Field()
    # g_reviever_helpfulvote = scrapy.Field()
    g_score = scrapy.Field()
    g_content_comment = scrapy.Field()
    pass
