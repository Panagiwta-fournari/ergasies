# coding=utf-8
import re
import urllib.request

url = input('Insert url to fetch: ')

if not url.startswith('http'):
    url = 'http://' + url
response = urllib.request.urlopen(url)
html = response.read().decode()

links_count = len(re.findall(r'<a .*?href=".*?".*?>.*?<\/a>', html))

newlines_count = len(re.findall(r'<br .*?/?>', html))
newlines_count += len(re.findall(r'<p .*?>.*?<\/p>', html))

print('There are %s links in the given webpage' % links_count)
print('There are %s newlines in the given webpage' % newlines_count)
