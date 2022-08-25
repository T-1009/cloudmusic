import re
import os
import requests

headers = {
    'User-Agent': 'Chrome/10'
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
}


def creat_file(filename):
    if not os.path.exists(filename):
        os.mkdir(filename)
    os.chdir(filename)


# 创建以歌手名字命名的文件夹
def creat_singer_name_folder(html_text):
    # <h2 id="artist-name" data-rid=5771 class="sname f-thide sname-max" title="许嵩 - Vae">许嵩</h2>
    singer_name_patt = re.compile(
        r'<h2 id="artist-name" data-rid=[0-9]* class="sname f-thide sname-max" title=".*?">(.*?)</h2>')
    singer_name = singer_name_patt.findall(html_text)[0]

    creat_file(singer_name)
    find_sing_id(html_text)


# https://music.163.com/#/song?id=167827
def find_sing_id(html_text):
    song_patt = re.compile(r'<li><a href="/song\?id=([0-9]*)">(.*?)</a></li>')
    song = song_patt.findall(html_text)
    for song_id, song_name in song:
        music_content = requests.get('https://music.163.com/#/song?id={song_id}', headers).content
        with open(song_name + 'm4a', 'wb') as f:
            f.write(music_content)
        print(song_id, song_name, '下载完毕!')


def main():
    print('许嵩的ID:5771')
    ID = input('请输入你喜欢的歌手的ID:')
    url = 'https://music.163.com/artist?id=' + ID
    html_text = requests.get(url, headers).text
    creat_singer_name_folder(html_text)

main()
