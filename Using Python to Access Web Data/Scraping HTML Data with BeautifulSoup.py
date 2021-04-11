# Write programe to read the HTML from the data files below, and parse the data, 
# extracting numbers and compute the sum of the numbers in the file.

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
'''
Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
sum=0
for tag in tags:
    sum= sum+ int(tag.contents[0])
print(sum)