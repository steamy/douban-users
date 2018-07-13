#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# Filename:  proxy_ip_spider.py
# Author： steam
# Time    : 2018/7/12 下午5:07

import scrapy
from ..items import ProxyIpSpiderItem

class ProxyIpSpider(scrapy.Spider):

    name = 'proxy'
    custom_settings = {
        'ITEM_PIPELINES': {
            'userSpider.pipelines.ProxyIpspiderPipeline': 300,
        }
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    def combain(self,domain, port, protocol='http'):
        # 验证ip是否可用
        return protocol.lower() + '://' + domain + ':' + port

    def start_requests(self):
        start_url = 'http://www.data5u.com/free/gngn/index.shtml'
        yield scrapy.Request(url=start_url, headers=self.header, callback=self.parse)


    def parse(self, response):
        proxyIpItem = ProxyIpSpiderItem()
        domains = response.selector.xpath('//ul[@class="l2"]//span[1]//li//text()').extract()
        ports = response.selector.xpath('//ul[@class="l2"]//span[2]//li//text()').extract()
        protocols = response.selector.xpath('//ul[@class="l2"]//span[4]//li//text()').extract()
        proxyIpItem['data5u_ips'] = list(map(self.combain, domains, ports,protocols))
        yield scrapy.Request(url='http://www.xicidaili.com/nn',headers=self.header,callback=self.parse_xici, meta={'item':proxyIpItem})

    def parse_xici(self, response):
        proxyIpItem = response.meta['item']
        domains = response.selector.xpath('//table[@id="ip_list"]//tr//td[2]//text()').extract()
        ports = response.selector.xpath('//table[@id="ip_list"]//tr//td[3]//text()').extract()
        protocols = response.selector.xpath('//table[@id="ip_list"]//tr//td[6]//text()').extract()
        proxyIpItem['xici_ips'] = list(map(self.combain,domains,ports,protocols))
        yield scrapy.Request(url='http://www.66ip.cn/areaindex_21/1.html', headers=self.header, meta={'item':proxyIpItem}, callback=self.parse_ip66)

    def parse_ip66(self, response):
        proxyIpItem = response.meta['item']
        domains = response.selector.xpath('//div[@align="center"]//table//tr//td[1]//text()').extract()
        ports = response.selector.xpath('//div[@align="center"]//table//tr//td[2]//text()').extract()
        proxyIpItem['ip66_ips'] = list(map(self.combain, domains, ports))
        proxyIpItem['ip66_ips'].remove('http://ip:端口号')
        return proxyIpItem

