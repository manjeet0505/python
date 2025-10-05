import threading
import time
import requests

def download(url):
    print(f"Starting downlaod from {url}")
    resp = requests.get(url);
    print(f"end of downlaoding , size = {len (resp.content)} bytes");

urls = [
    "https://www.pixelstalk.net/wp-content/uploads/2016/07/3840x2160-Images-Free-Download.jpg",
    "https://tse3.mm.bing.net/th/id/OIP.MCLzVoExgXPyNi_V5gb1AwHaE7?pid=Api&P=0&h=180"
]

start = time.time();

threads = [];

for url in urls:
    t = threading.Thread(target = download, args = (url , ))
    t.start()
    threads.append(t)

for t in threads:
    t.join();

end = time.time();

print(f"all downloads {end - start:.2f} seconds")
         