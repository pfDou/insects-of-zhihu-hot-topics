# -*- coding: utf-8 -*-  

import urllib.request
from bs4 import BeautifulSoup
import re

main_page = "http://www.zhihu.com/explore#daily-hot"

urllines = urllib.request.urlopen(main_page)
page_data = urllines.read()
urllines.close()
soup = BeautifulSoup(page_data)

#f = open("zhihu.txt","w")


hot_topics = soup.find('div',  attrs = {"data-type":"daily"})
hot_topics.decode('utf-8').encode('gbk')
#f.write(str(hot_topics))

print(hot_topics)
topic = hot_topics.find_all('h2', attrs = {"class":"question_link"})
#topic_href = topic['href']
print(topic)