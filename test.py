from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
#tạo kết nối
conn = urlopen(url)

#đọc data
raw_data = conn.read()
#decode data
content = raw_data.decode("utf8")
#mở-ghi-đóng file tải về
with open("sua.html", "wb") as f:
    f.write(raw_data)
    f.close()
print(f)
#find ROI
soup = BeautifulSoup(content, "html.parser")
ul_new = soup.find("div", style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
li_list = ul_new.find_all("tr")

# print(li_list)
# for td in li_list:
n = li_list[0]

print(n)
