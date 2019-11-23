import urllib.request
import urllib.parse
url = 'https://www.iqianyue.com/mypost'
postdata =urllib.parse.urlencode({
    "name":"abc",
    "pass":"124"
}).encode('utf-8')
req = urllib.request.Request(url,postdata)
req.add_header=("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
data = urllib.request.urlopen(req).read()
fhandle = open("iqianyue.html","wb")
fhandle.write(data)
fhandle.close()