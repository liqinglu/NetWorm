#coding:utf-8
import urllib2
import re
import sys
import httplib
httplib.HTTPConnection._http_vsn = 10 
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'

#proxy_info = {
#	'user' : '******' ,
#	'pass' : '******' ,
#	'host' : '135.251.33.15' ,
#	'port' : 80
#}
##build a new opener that uses a proxy requiring authorization
#proxy_support = urllib2.ProxyHandler( {"http" : "http://%(user)s:%(pass)s@%(host)s:%(port)d" % proxy_info} )
#opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
##install it
#urllib2.install_opener(opener)

url = "http://haiku-lu.blogbus.com/index_%d.html"
fname = "myblog%d.html"
dname = "detail%d.html"
foutput = "record.txt"
reload(sys)
allpages = 5

all = []

for idx in range(1,allpages+1):
    myurl = url%idx
    content = urllib2.urlopen(myurl).read()
    filename = fname%idx
    open(filename,'w').write(content)

    readingdetail = '<div.*?class="menubar"><span.*?href.*?href=\'(.*?)\'.*?class='
		#myItems = re.findall('<div.*?class="postHeader">.*?<h3>(.*?)</h3>',content,re.S)
    #myItems = re.findall('<div.*?class="postHeader">.*?<h3>(.*?)</h3>.*?<h2><a href=.*?>(.*?)</a></h2>',content,re.S)
    #myItems = re.findall('<div.*?class="postBody">(.*?)<div.*?class="clear">',content,re.S)
    myItems = re.findall(readingdetail,content,re.S)
    for subidx in range(1,len(myItems)+1):
				all.append(myItems[subidx-1])

for idx in range(1,len(all)+1):
		detailcontent = urllib2.urlopen(all[idx-1]).read()
		detailf = dname%(idx)
		open(detailf,'w').write(detailcontent)
		dsearch = '<div.*?class="postHeader".*?<h3>(.*?)</h3>.*?<h2>(.*?)</h2>.*?<div.*?class="postBody".*?href=.*?href=.*?href=.*?</a><br.*?/><br.*?/>.*?</p><p>(.*?)<style>'
		dItems = re.findall(dsearch,detailcontent,re.S)
		myop = open(foutput,'a')
		sys.setdefaultencoding('utf-8')
		for item in dItems:
				for each in item:
						myop.write(each.strip())
						myop.write('\n')
				myop.write('\n')
		
		myop.close()