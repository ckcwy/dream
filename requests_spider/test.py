import sys,os,requests
from lxml import etree
#path=os.path.abspath('.')
#os.mkdir(path+'/testdir')
sys.setrecursionlimit(1000)



url='http://www.mzitu.com/'
response=requests.get(url)
html=etree.HTML(response.content)
urls=html.xpath(".//ul[@id='menu-nav']//a/@href")[1:5]
titles=html.xpath(".//ul[@id='menu-nav']//a/text()")[1:5]
#print(urls)
#response=requests.get(url_xinggan)
#html=etree.HTML(response.content)
#web=html.xpath(".//div[@class='nav-links']//a[contains(text(),'下一页')]/@href")
#print(web)
#print(titles)
path=os.path.abspath('.')
os.mkdir(path+'\\pics')

webs=[]
def get_cur_page(url):
	response=requests.get(url)
#	print(response.url)
	webs.append(url)
	html=etree.HTML(response.content)
	links=html.xpath(".//div[@class='nav-links']//a[contains(text(),'下一页')]/@href")
	if len(links) <1:
		pass
	else:
		get_cur_page(links[0])
m=1
for i in range(4):
	get_cur_page(urls[i])


	path=os.path.abspath('.')+'\\pics'
	os.mkdir(path+'\\%s'%titles[i])
	path=path+'\\%s'%titles[i]+'\\{}'
	for web in webs:
		print(web)
		response=requests.get(web)
		html=etree.HTML(response.content)
		imgs=html.xpath(".//ul[@id='pins']//img/@src")
		for img in imgs:
			filename=img.split('/')[-1]
			file_content=requests.get(img)
			try:
				with open(path.format(filename),'wb') as f:
					f.write(file_content.content)
			except:
				print(filename)
			print(m)
			m+=1
