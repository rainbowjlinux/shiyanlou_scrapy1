#!/usr/bin/env python3
#-*- coding:utf-8 -*-
############################
#File Name: course_spider.py
#Created Time: 2017-11-17 16:00:07
#Author: rainbowjlinux
############################

import scrapy

class course_spider(scrapy.Spider):

    name = 'course-spider'

    @property
    def start_urls(self):
        url_page = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        return (url_page.format(i) for i in range(1, 24))

    def parse(self, response):
        for course in response.css('div.course-body'):
            yield {
                'name': course.css('div.course-name::text').extract_first(),
                'description': course.css('div.course-desc::text').extract_first(),
                'type': course.css('div.course-footer span.pull-right::text').extract_first(default='免费'),
                'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d*)[^\d]*')
            }
