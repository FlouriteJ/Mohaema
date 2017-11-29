global URLs
global Texts
URLs=[]
Texts=''

def get_chars(_str):#Return <str>
	import re
	_list=re.findall(r"(?:<p align=\"justify\">)(.+?)(?:</p>)",_str)
	_list2=re.findall(r"(?:<div>)(.+?)(?:</div>)",_str,re.DOTALL)
	_list.extend(_list2)
	return '\n'.join(_list)

	
def read_url(_url):#Return <str>
	import urllib.request
	import random
	_req = urllib.request.Request(url=_url,headers={'User-Agent': 'Smart Boy'+str(random.random())})
	return urllib.request.urlopen(_req).read().decode("utf-8", "ignore")

	
def get_urls(_str):#Return <list>
	import re
	return list(set(re.findall(r"(?:href=\"\.)(/.+html)",_str)))
	

def url_visit(ori_url):
	global URLs
	global Texts
	_data=read_url(ori_url)
	_urllist=get_urls(_data)
	Texts=Texts+url_cleaning(get_chars(_data))+'\n'
	for i in _urllist:
		if 'index.html' in ori_url:
			_url2='%s%s'%(ori_url[:len(ori_url)-11],i)
		if not _url2 in URLs:
			URLs.append(_url2)
	
	return
	

def url_cleaning(_str):#Return <str>
	import re
	_str=_str.replace('','')
	_str=_str.replace('&nbsp;','')
	_str=re.sub(r'<.+?>','',_str)
	_str=re.sub(r'\\u\d+?','',_str)
	_list=_str.split('\n')
	_str='\n'.join([i for i in _list if i!='' and i!='\n'])
	return _str


URLs.append('http://www.g20.org/index.html')
#URLs.append('http://www.g20.org/hywj/lnG20gb/201511/t20151106_1237.html')
URLs_counter=0
while URLs_counter!=len(URLs):
	print(URLs[URLs_counter])
	#try:
	url_visit(URLs[URLs_counter])
	#except:
	#	print('Error:↑')
	URLs_counter+=1
print(Texts)
_file=open('url_3.txt','w')
_file.write('\n'.join(URLs))
_file.close()
_file=open('G20_3.txt','w')
_file.write(Texts)
_file.close()
input()
input()