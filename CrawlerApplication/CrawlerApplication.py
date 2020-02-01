import requests
import time
from bs4 import BeautifulSoup, SoupStrainer
 
# textからlistとかに変換
url = "https://s.fudousan.or.jp/system/?act=l&type=31&pref=13&stype=l&city[]=13101&n=20&p=1&v=on&s="
url2 = "https://s.fudousan.or.jp/system/?act=l&type=31&pref=13&stype=l&city[]=13101&n=20&p=2&v=on&s="
 
# Webサイトからデータ取得
response = requests.get(url)
response.encoding = response.apparent_encoding

# コンソール出力
#print(response.text)


# 1秒開ける。
#time.sleep(1)

# 2個目以降のデータ取得
#response2 = requests.get(url2)
#response2.encoding = response.apparent_encoding


#物件名パース
use_parser = "lxml"

parse_only_header = SoupStrainer("div", class_="tit-syousai")
print(BeautifulSoup(response.text, use_parser , parse_only=parse_only_header).prettify())

#詳細情報パース
parse_only_info = SoupStrainer("td")
print(BeautifulSoup(response.text, use_parser , parse_only=parse_only_info).prettify())




# 加工処理

# 標準のパーサー(Python’s html.parser)を利用
# http://kondou.com/BS4/#id47
# ただ、本来はドキュメントの一部だけ取ってきてパースすべき
#bs = BeautifulSoup(response.text, 'html.parser')





#bs_ul = bs.find('span')
 
# listがゼロ件だとErrorになるので注意
#for bs_li in bs_ul.find_all('li'):
#    bs_text = bs_li.text
#    print(bs_text)
 

# 特定タグ名がある要素を全部表示させるやつ。
#for i in bs.select("span"):
#    print(i.getText())