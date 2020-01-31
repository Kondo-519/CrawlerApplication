import requests
import time
 
# textからlistとかに変換
url = "https://s.fudousan.or.jp/system/?act=l&type=31&pref=13&stype=l&city%5B%5D=13101"
 
response = requests.get(url)
response.encoding = response.apparent_encoding
 
print(response.text)
