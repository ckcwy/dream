import os,requests
from lxml import etree
#爬图片

#response=requests.get(host)
#html=etree.HTML(response.content)
#links=html.xpath(".//div[@class='page']//a[contains(text(),'下一页')]/@href")
webs=[]
def get_alldata(url):
	response=requests.get(url)
	webs.append(url)
	html=etree.HTML(response.content)
	links=html.xpath(".//div[@class='page']//a[contains(text(),'下一页')]/@href")
	if len(links)<1:
		pass
	else:
		host='http://www.qiubaichengren.net/'
		host+=links[0]
		get_alldata(host)
get_alldata('http://www.qiubaichengren.net/')

for web in webs:
	response=requests.get(web)
	html=etree.HTML(response.content)
	imgs=html.xpath(".//div[@class='ui-module']//img/@src")
	#print(imgs,len(imgs))

	for i in imgs:
		filename=i.split('/')[-1]
		filecontent=requests.get(i)
		path=os.path.abspath('.')
		path+='/pics/{}'
		try:
			with open(path.format(filename),'wb') as f:
				f.write(filecontent.content)
		except:
			print(filename)

