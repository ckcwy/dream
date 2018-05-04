import sys,os,requests
from lxml import etree
url='http://www.mzitu.com/'
response=requests.get(url)
html=etree.HTML(response.content)
urls=html.xpath(".//ul[@id='menu-nav']//a/@href")[1:5]
titles=html.xpath(".//ul[@id='menu-nav']//a/text()")[1:5]


path=os.path.abspath('.')
os.mkdir(path+'\\pics')
path=os.path.abspath('.')+'\\pics\\'

for m in titles:
	os.mkdir(path+'\\%s'%m)
