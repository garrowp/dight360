import requests as r

khmer_url = 'https://en.wikipedia.org/wiki/Khmer_language'
headers = {'user-agent': 'Peter Garrow (garrowp@byu.edu)'}
response = r.get(khmer_url, headers=headers)
with open('khmer_language.html', 'w') as my_file:
    print(response.text, file=my_file)
