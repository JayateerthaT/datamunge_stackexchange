from scrapy import Spider
from scrapy.selector import Selector
from scrapy import Request
from stack.items import StackItem


class StackSpider(Spider):
	name = "stack"
	allowed_domains = ["stackoverflow.com"]
	start_urls = ["http://stackoverflow.com/questions?pagesize=50&sort=newest"]

	def parse(self, response):
		#questions = Selector(response).xpath('//div[@class="summary"]/h3')
		questions = Selector(response).xpath('//div[@class="summary"]')
		
		for question in questions:
			tag=''
			item = StackItem()
			item['title'] = question.xpath('h3/a[@class="question-hyperlink"]/text()').extract_first()
			item['url'] = question.xpath('h3/a[@class="question-hyperlink"]/@href').extract_first()
			item['description'] = question.xpath('div[@class="excerpt"]/text()').extract_first()
			questiontags = question.xpath('div/a[@class="post-tag"]')
			for questiontag in questiontags:
				tag = tag + questiontag.xpath('text()').extract_first() + ','

			item['questiontag'] = tag 
			yield item
		##next_page
		#next_page_url = response.xpath('//*[@class="page-numbers next"]/text()/../../@href').extract_first()
		##print('Processing..' + next_page_url)
		#next_absolute_page_url = response.urljoin(next_page_url)
		##print('Processing..' + next_absolute_page_url)
		#yield Request(next_absolute_page_url, callback=self.parse)

