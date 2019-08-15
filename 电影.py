import requests
import os
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

url = 'https://zkgn.wb699.com/2018/07/17/a2GwZ0N7l83CjeSR/out{}.ts'



i=0
while i<=999:
    a='00'+str(i)
    k=a[-3:]
    nuw_url=url.format(k)
    print(nuw_url)
    i+=1
#     print(a)
    response = requests.get(url=nuw_url, headers=headers)
    with open('行尸走肉第四季\第三集.mp4','ab') as f:
        f.write(response.content)
print('爬取结束')