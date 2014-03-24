import urllib2
opener = urllib2.build_opener()
html = opener.open('https://gree-native.atlassian.net/issues/?filter=10403').read()

from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(html)
print soup.find('tr',)