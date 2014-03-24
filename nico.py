#-*- coding: utf-8 -*-
import urllib, urllib2, cookielib, re

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

mail = 'green910x@yahoo.co.jp' # type your own username
password = '' # password
flv_id = 'sm18115902'

r = opener.open("https://secure.nicovideo.jp/secure/login", "mail=%s&password=%s" % (mail, password))

r = opener.open("http://www.nicovideo.jp/api/getflv?v=" + flv_id)
params = re.compile("([^&]+)=([^&]*)").findall(r.read())
params = dict(params)
flv_url = urllib.unquote(params["url"])

r = opener.open("http://www.nicovideo.jp/watch/" + flv_id)

# ファイルをダウンロード
f = open(flv_id + ".flv", "wb")
r = opener.open(flv_url)
f.write(r.read())
f.close()