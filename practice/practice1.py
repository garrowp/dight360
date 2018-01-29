import re
import requests as r  # requests is not in standard library: $ pip3 install requests

joke_url = 'https://www.rd.com/jokes/halloween-jokes-for-kids/'
headers = {'user-agent': 'Robert Reynolds (garrowp@byu.edu)'}
response = r.get(joke_url, headers=headers)
str_text = response.text
print(str_text)
# print(response.text, '....')
str_re = r'<article.*?<div class="content-wrapper"><p>(.*?)</p>.*?</article>'
result = re.findall(str_re, str_text, re.S)
print(result)
print()