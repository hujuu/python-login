import urllib2

url = 'https://www.hatena.ne.jp/login'

name = 'hujuu' # type your own username
password = '' # password

req = urllib2.Request(url, 'name=%s&password=%s' % (name, password))
#req.add_header('hoge', 'fuga')
cont = urllib2.urlopen(req).read()

f = open('out.html', 'w')
f.write(cont)
f.close()