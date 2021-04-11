# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and 
# extract the comment counts from the JSON data, compute the sum of the numbers in the file
'''
Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1193253.json (Sum ends with 66)
'''

import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter URL ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
#print(info)
sum=0
for comment in info["comments"]:
    sum+=int(comment['count'])
print('sum',sum)