import urllib2
import cookielib

name = 'hujuu'
password = '07649vb'


url = 'https://www.hatena.ne.jp/login'
req = urllib2.Request(url, 'name=%s&password=%s' % (name, password))
#req.add_header('hoge', 'fuga')

opener = urllib2.build_opener()
opener.add_handler(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))

conn = opener.open(req)

url = 'http://blog.hatena.ne.jp/%s/' % name
req = urllib2.Request(url)
conn = opener.open(req)

cont = conn.read()

f = open('out.html', 'w')
f.write(cont)
f.close()