# -*- coding: utf-8 -*-

import requests
import time
import re
# スクレイピング用
from bs4 import BeautifulSoup
# URL取得
url = u"http://www.boatrace.jp/owpc/pc/extra/data/download.html"
# リンク指定用正規表現
pattern = r"href=\".+\.lzh\""
repeat = re.compile(pattern)
href = ""
link = ""
m = ""
file_name = ""
# urlからhtml取得
r = requests.get(url)
# 中身の読み込み
soup = BeautifulSoup(r.content,"html.parser")
# ulタグの取得
src = soup.find_all('ul',class_="data_list h-mt15")
# 文字列にしてもう一度読み込み
soup2 = BeautifulSoup(str(src),"html.parser")
# aタグ取得
src = soup2.find_all('a')

for m in src:
 # 一秒スリープ
 time.sleep(1)
 # href要素取得
 link = m.get('href')
 r = requests.get("http://www.boatrace.jp" + link)
 # ファイル名取得
 file_name = link.split("/")[-1]
 # ダウンロード成功の場合：書き込み
 if r.status_code == 200: # HTTPステータスコード 100:処理中,200:成功,300:リダイレクト,400:クライアントエラー,500:サーバーエラー
   f = open("boat-racer_lzh/" + file_name,'wb')
   f.write(r.content)
   f.close()
   print(file_name + " ダウンロード完了")
