#-8- coding:utf-8 -*-
import requests
import re
import time
import json


#获取单页信息
def get_one_page(url):
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
	response=requests.get(url=url,headers=headers)
	if response.status_code==200:
		return response.text
	else:
		return None
	
#解析单页信息
def parse_one_page(html):
	pattern=re.compile('<table width="100%">.*?title="(.*?)"\n.*?class="pl">(.*?)</p>.*?"rating_nums">(.*?)</span>.*?<span class="pl">\(\n(.*?)</span>',re.S)
	items=re.findall(pattern,html)
	for item in items:
		yield item

#保存信息
def write_to_file(content):
	with open('doubanbook_top250.txt','a',encoding='utf-8') as f:
		f.write(json.dumps(content,ensure_ascii=False)+'\n')

#调用函数
def main(start):
	url='https://book.douban.com/top250?start='+str(start)
	html=get_one_page(url)
	for item in parse_one_page(html):
		print(item)
		write_to_file(item)

#循环爬取多页信息
if __name__=='__main__':
	for i in range(10):
		main(start=i*25)
		time.sleep(1)
