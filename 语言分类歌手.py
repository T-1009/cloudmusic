# [^\x00-\xff]
import re
import requests


headers = {
    # 'User-Agent': 'Mozilla/6.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
    'User-Agent': 'Chrome/10'
}

# https://music.163.com/#/discover/artist/cat?id=1001
'''
    <li><a href="/discover/artist/cat?id=1001"
    class="cat-flag z-slt"
    data-cat="1001">华语男歌手</a>
    </li>
'''

# 语种下歌手分类
# url = 'https://music.163.com/discover/artist/cat?id='
url_singers_id = 'https://music.163.com/discover/artist/'

singers_id_patt = re.compile(r'<li><a href="/discover/artist/cat\?id=(\d*)')
singers_id_html_text = requests.get(url_singers_id, headers).text
singers_id = singers_id_patt.findall(singers_id_html_text)


# 各语种下歌手具体分类
# https://music.163.com/#/discover/artist/cat?id=1001&initial=65
# url_singer_id = 'https://music.163.com/discover/artist/cat?id={}&initial={}'.format(id, letter)
# <a href=" /artist?id=12174057" class="nm nm-icn f-thide s-fc0" title="艾辰的音乐">艾辰</a>
# <a href="/discover/artist/cat?id=1001&initial=90" class="">Z</a>
letter_patt = re.compile(r'<a href="/discover/artist/cat\?id=\d*&initial=(\d*)" class=".*?">.*?</a>')
url_letter = 'https://music.163.com/discover/artist/cat?id=1001&initial=65'
letter_html_text = requests.get(url_letter, headers).text
letter = letter_patt.findall(letter_html_text)


print(singers_id)
print(letter)


for id in singers_id:
    for initial in letter:
        url_singer_id = 'https://music.163.com/discover/artist/cat?id={}&initial={}'.format(int(id), int(initial))
        singer_patt = re.compile(r'<a href=".*?/artist\?id=(\d*)" class="nm nm-icn f-thide s-fc0" title=".*?">(.*?)</a>')
        singer_html_text = requests.get(url_singer_id, headers).text
        singer = singer_patt.findall(singer_html_text)
        print(singer)
        with open('singer.txt', 'a', encoding='utf-8') as f:
            for i in singer:
                f.write(str(i) + '\n')