import requests
import os
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

url = 'https://zkgn.wb699.com/2018/07/17/{}/out{}.ts'


'https://zkgn.wb699.com/2018/07/17/Kvay9SVXN9hhouYZ/out000.ts'

zdlist={'1':'Kvay9SVXN9hhouYZ','2':'9bfjzGo8R4xLoF7G','3':'IDb4O3t8ReF1CSZe','4':'dr008nHCeaNx6EUQ','5':'IXzUguZPZCn6DOUs',
        '6':'sEV55FsOIXFSjfqJ','7':'0upDBA84aaFrhOAY','8':'RttNUGlazdZI61Ck','9':'ZIwtGr4D0sXzhhPZ','10':'Kbbqt3TBT2ZoJs12',
        '11':'y0Hj3OCU5BTPzuzY','12':'CEH5eZzOM8vJ9VN4','13':'VYQ5pGpa96gjXQrb','14':'Wo6Xjku1nwz2HOMi','15':'aukm3wEGxf5X7Jmh',
        '16':'WheDv0ejrFV3GdjE'}

for k,v in zdlist.items():
    # print(k,v)
    a_url='https://zkgn.wb699.com/2018/07/17/{}'.format(v)+'/out'
    # print(a_url)
    i=0
    while i<=500:
        a='00'+str(i)
        c=a[-3:]
        nuw_url=a_url+c+'.ts'
        print(nuw_url)
        i+=1
        try:
            response = requests.get(url=nuw_url, headers=headers)
            with open('行尸走肉第五季\第{}集.mp4'.format(k),'ab') as f:
                f.write(response.content)
        except:
            pass
    print('爬取结束')