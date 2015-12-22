# -*- coding: utf-8 -*-

import scrapy

from searchpy.items import SearchpyItem
import sys
import string 

sys.stdout=open('output.txt','w')

class SearchpySpider(scrapy.Spider):
	
	
	name = "searchpy"
	
	allowed_domains = ["searchpy.org"]
	start_urls = []
	for i in range(1,10):
		start_urls.append("http://so.csdn.net/so/search/s.do?p=%d&q=python&t=blog"%i)
	
	def parse(self,response):
		filename = response.url.split("/")[-1][7]
		with open(filename,'wb') as f:
			f.write(response.body)
			f.close()
		#filename = response.url.split("/")[-2]
		for sel in response.xpath('//dl[re:test(@class,"search-list")]/dd[re:test(@class,"search-link")]'):
			item = SearchpyItem()
			item['name'] = sel.xpath('a/text()').extract()
			item['url'] = sel.xpath('a/@href').extract()
			item['description'] = sel.xpath('text()').extract()
			with open(filename,'wb') as f:
				f.write("%s"%sel.xpath('a/@href').extract())
			#print sel.xpath('a/@href').extract()
			#print sel.xpath('//dl[re:test(@class,"search-list")]')