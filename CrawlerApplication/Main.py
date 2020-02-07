import os

# SiteURLからアクセス対象のURLを読み込む。
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SiteURL.txt")

with open(path) as f:
    siteList = f.readlines()

# クローリングして、Jsonのリストを作成する。
#TOPを読み込む。
#要素を分解する。
#１秒？待機。
#個別ページを読み込む。
#詳細情報を継ぎ足す。
#１秒？待機

# DBに更新をかけにいく。


print(type(siteList))
print(siteList)