from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
# open connection
conn = urlopen(url)
# read data
raw_data = conn.read()
# decode data
content = raw_data.decode("utf8")
with open("nhac.html","wb") as f:
    f.write(raw_data)
# find ROI
soup = BeautifulSoup(content, "html.parser")
ul = soup.find("ul", "")
#copy and save
li_list = ul.find_all("li")
new_list = []
for li in li_list:
    h3 = li.h3
    a = h3.a
    title = a.string
    h4 = li.h4
    a = h4.a
    artist = a.string
    songs = {
        "title": title,
        "artist": artist,
    }
    new_list.append(songs)
pyexcel.save_as(records = new_list, dest_file_name = "demo.xlsx")
#dowload youtube
options = {
    "default_search": "ytsearch",
    "max_dowload": 100,
    "format":"bestaudio/audio",
}
dl = YoutubeDL(options)
# for i in new_list:
#     key = i["title"]
#     print(key)
#     dl.download([key])
for i in new_list:
    print(i["title"])
    dl.download(i["title"])


