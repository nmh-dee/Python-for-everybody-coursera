# The program will prompt for a URL, read the XML data from that URL using urllib 
# and then parse and extract the comment counts from the XML data, 
# compute the sum of the numbers in the file.

'''
Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1193252.xml (Sum ends with 25)
'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
sum=0
items = tree.findall('comments/comment')
for item in items:
    sum+= int(item.find('count').text)
print(sum)
