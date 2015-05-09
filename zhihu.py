# -*- coding: utf-8 -*- 


import urllib.request
from bs4 import BeautifulSoup
import re

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding="utf8")

main_page = "http://www.zhihu.com/explore#daily-hot"

urllines = urllib.request.urlopen(main_page)    #<class 'http.client.HTTPResponse'>
page_data = urllines.read()						#<class 'bytes'>
urllines.close()
soup = BeautifulSoup(page_data)					#<class 'bs4.BeautifulSoup'>

#f = open("zhihu.txt","w")


hot_topics = soup.find('div',  attrs = {"data-type":"daily"}).children
output = []


for item in list(hot_topics):
	if item.string:
		pass	# navigableString type, maybe space line in the source page
	else:
		output.append({})
		q_index = int(item["data-offset"])-1
		print(item["data-offset"])
		href = item.h2.a["href"]
		question = item.h2.a.string
		print("Question:", question)

		#answer page's url
		url = "http://www.zhihu.com" + href
		print("answer address:",url)

		#open answer page get the answer
		sub_urllines = urllib.request.urlopen(url)    #<class 'http.client.HTTPResponse'>
		sub_page_data = sub_urllines.read()						#<class 'bytes'>
		sub_urllines.close()
		sub_soup = BeautifulSoup(sub_page_data)
		# print(sub_soup.title)

		favorer_num = sub_soup.find("span", class_="count").text
		print("favorer_num:",favorer_num)
		brief_Q = sub_soup.find("div", class_="zm-editable-content").text
		print("Question's brief:",brief_Q)
		# test = sub_soup.find_all("div", attrs={"class":"zm-editable-content"})
		# for i in test:
		# 	print(i["class"])

		answer_head = sub_soup.find("div", class_="answer-head")
		
		author = sub_soup.find("a", class_="zm-item-link-avatar").next_sibling.next_sibling.string
		print("author:", author)
		author_qg = sub_soup.find("a", class_="zm-item-link-avatar").next_sibling.next_sibling.next_sibling.next_sibling.string
		print("author's qg:", author_qg)
		#answer = sub_soup.find_all("div", attrs={"class":"zm-editable-content"})[2].text#get_text()
		answer = sub_soup.find("div", class_=" zm-editable-content clearfix").text
		print("Answer:", answer)




