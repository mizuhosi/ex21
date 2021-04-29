import requests
from bs4 import BeautifulSoup
import datetime
import schedule
import time
import os.path

# 検索ワード
serchword = 'japan'
url = f'https://news.google.com/search?q={serchword}&hl=ja&gl=JP&ceid=JP:ja'

if os.path.isdir('out') == False:
    os.mkdir('out')

# スクレイピングを行う
def getnews():
    r = requests.get(url)
    html = r.text

    # BSを利用してWebページを解析する
    soup = BeautifulSoup(html, 'html.parser')
    elems = soup.select('article h3 a')

    fn = f'./out/{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}.txt'

    # ニュースのタイトルを出力する
    with open(fn, mode='w') as f:
        for e in elems:
            f.write(e.getText() + '\n')

# 2分沖にスケジュールを定義
schedule.every(2).minutes.do(getnews)

while True:
    schedule.run_pending()
    time.sleep(1)