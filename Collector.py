from asyncio import as_completed
from Downloader import Downloader
import requests
from requests.models import Response
import time
from typing import Iterable, Set
import tqdm
from config import config
import concurrent.futures as  futures
class Collector:
     def __init__(self,downloader:Downloader): 
         self.pids_g: Set[str]=set()
         self.downloader=downloader
     def add(self,args: Iterable[str]):
      for pid in args:
          self.pids_g.add(pid)
     def select_url(self,response:Response):
          image_urls=set()
          for url in response.json()['body']:
              image_urls.add(url['urls']['original'])
          return image_urls
     def collect_url(self,url,sellector,additional_header):
          headers=config.header_u
          if additional_header is not None:
              headers.update(additional_header)
          time.sleep(1)
          for i in range(10):
              try:
                response=requests.get(url,headers=headers,proxies=config.proxy)
                if response.status_code==200:
                    urls=sellector(response)
                    return urls
              except Exception as e:
                    time.sleep(1)
     def collect(self):
         #sample url: https://www.pixiv.net/ajax/illust/xxxx/pages?lang=zh
           print("===== Collector start =====")
           with futures.ThreadPoolExecutor(8) as executor:
               with tqdm.trange(len(self.pids_g),desc="collecting url") as pb:
                urls=[f"https://www.pixiv.net/ajax/illust/{pid}/pages?lang=zh" for pid in self.pids_g]
                colloctor_headers=[{
                    'Cookie': config.cookie,
                    'Referer': f'https://www.pixiv.net/artworks/{pid}',
                    'x-user-id': config.user_id,
                    }
                     for pid in self.pids_g]
                urls_fu=[
                    executor.submit(self.collect_url,url,self.select_url,aditional_header)for url, aditional_header in zip(urls,colloctor_headers)]
                for future in futures.as_completed(urls_fu) :
                    urls=future.result()
                    if urls is not None:
                        self.downloader.add_url(urls)
                    pb.update()
           print("===== Collector finished =====")

