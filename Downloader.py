from typing import Set
from asyncio import futures
from logging import captureWarnings
from config import config
import re
import os
import requests
import concurrent.futures as futures
import tqdm
import time

class Downloader:
    def __init__(self,cap:float):
        self.urls: Set[str]=set()
        self.cap=cap
    def add_url(self,urls):
        for url in urls:
            self.urls.add(url)
    def download_image(self,url):
        # sample : https://i.pximg.net/img-original/img/2024/01/19/00/00/33/115282690_p0.jpg
        pattern = r'[^/]+\.(?:jpg|jpeg|png|gif|webp)(?=\?|$)'
        match = re.search(pattern, url)
        if match:
             filename = match.group()
        match = re.search(r'/(\d+)_p\d', url)
        if match:
            image_id = match.group(1)
        if os.path.exists(filename):
            return 0
        headers=config.header_u
        headers.update({'Referer':f"https://www.pixiv.net/artworks/{image_id}",
                         'Cookie':config.cookie})
        time.sleep(1)
        for i in range(10):
             try :
                response=requests.get(url,headers=headers,proxies=config.proxy)
                if response.status_code==200:
                    if "content-length" not in response.headers :
                        raise "content-length not in response.headers"
                    image_size=int(response.headers["content-length"])
                    with open(os.path.join(config.store_path,filename),'wb') as f:
                        f.write(response.content)
                    return image_size/(1<<20)
             except Exception as e:
                  time.sleep(1)
    def download(self):
        image_size=0.0
        print("===== Downloader start =====")
        with futures.ThreadPoolExecutor(8) as executor:
            with tqdm.trange(len(self.urls),desc="Downloading") as pb:
                image_size_fu=[executor.submit(self.download_image, url)for url in self.urls]
                for future in futures.as_completed(image_size_fu):
                    image_size+=future.result()
                    pb.set_description(f"Downloading {image_size:.2f} MB")
                    pb.update()
                    if image_size>=self.cap:
                        executor.shutdown(wait=False,cancel_futures=True)
                        break
        print("===== Downloader finished =====")




