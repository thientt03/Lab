from youtube_dl import YoutubeDL
#sample 1: dowload a single youtube video
dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=ZVZbjw9Dk7Y"]) # phải nhớ đặt video ở list ngay cả khi nó được tải xuống

#sample 2: dowload multiple youtube video
dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=ZVZbjw9Dk7Y","https://www.youtube.com/watch?v=jRPjLb3ZjCo"]) # đặt list các danh sách url tải xuống

#sample 3: dowload audio
options = {
    "format": "bestaudio/audio" # chỉ tải xuống chất lượng âm thanh tốt nhất 
}
dl = YoutubeDL(options)
dl.download(["https://www.youtube.com/watch?v=_MM1MQgFjRM"])

#sample 4: search and dowload the first video
options = {
    "default_search": "ytsearch", # nói với trình tải xuống tìm kiếm thay vì tải trực tiếp
    "max_dowloads": 1 # vị trí tải là thứ nhất
}
dl = YoutubeDL(options)
dl.download(["XIN-Nhóm Nhạc..."])
print(dl)

# sample 5: search and dowload the first audio
options = {
    "default_search": "ytsearch",
    "max_dowloads": 1,
    "format": "bestaudio/audio",
}
dl = YoutubeDL(options)
dl.download(["FBBOIZ-Để Em Rời Xa"])