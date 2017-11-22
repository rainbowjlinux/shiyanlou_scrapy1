#!/usr/bin/env python3
#-*- coding:utf-8 -*-
############################
#File Name: course_spider.py
#Created Time: 2017-11-17 16:00:07
#Author: rainbowjlinux
############################

import scrapy

class course_spider(scrapy.Spider):

    name = 'repository-spider'

    @property
    def start_urls(self):
        url_page = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_page.format(i) for i in range(1, 5))

    def parse(self, response):
        for course in response.xpath('//li[contains(@class, "col-12")]'):
            yield {
                'name': course.xpath('.//div/h3/a/text()').re_first('(\S+)'),
                'update_time': course.xpath('.//div/relative-time/@datetime').extract_first()
            }
