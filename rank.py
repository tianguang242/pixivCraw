import concurrent
from typing import Set
import datetime
import requests
import os
import json
from config import config
from Collector import Collector
from Downloader import Downloader
import re
import concurrent.futures as furtures
import time
import tqdm
class Rank:
    
    def __init__(self,cap:float=1024):
        self.urls_c: Set[str]=set()
        self.model=config.modle
        self.content=config.content
        self.cap=cap
        self.downloader=Downloader(200)
        self.collector=Collector(self.downloader)
    def collect_url(self,url,additional_header):
            headers=config.header_u
            if additional_header is not None:
                headers.update(additional_header)
            time.sleep(1)
            for i in range(10):
                try:
                    response=requests.get(url,headers=headers,proxies=config.proxy)
                    if response.status_code==200:
                        pids=set()
                        for pid in response.json()['contents']:
                          pids.add(pid['illust_id'])
                        return pids
                except Exception as e:
                        time.sleep(1)
    def rank_url(self):
        #sample : https://www.pixiv.net/ranking.php?mode={mode}&content={content}&date={date}
        # sample : https://www.pixiv.net/ranking.php?mode={mode}&content={content}&date={date}&p={page}&format=json
        date_o=datetime.datetime.strptime(config.collecttime,'%Y-%m-%d')
        date_list=[]
        for i in range(config.relativeday):
            date_lo=date_o -datetime.timedelta(days=i)
            date_list.append(date_lo.strftime('%Y%m%d'))
        for page in range(1,config.rank//50+2):
            for date in date_list:
                url=f"https://www.pixiv.net/ranking.php?mode={self.model}&content={self.content}&date={date}&p={page}&format=json"
                self.urls_c.add(url)
        try:        
            aditional_header=[{
                 'Referer': url.split('&p')[0],
                 'x-requested-with': 'XMLHttpRequest',
                 'Cookie': config.cookie,
                    }for url in self.urls_c]
            print("===== Rank Collector start =====")
            with furtures.ThreadPoolExecutor(8) as executor:
                with tqdm.trange(len(self.urls_c),desc="Collecting rank urls") as pb:
                    futures_list=[
                        executor.submit(self.collect_url,url,aditional_header)for url, aditional_header in zip(self.urls_c,aditional_header)]
                    for future in furtures.as_completed(futures_list):
                        pids=future.result()
                        if pids is not None:
                            self.collector.add(pids)
                        pb.update()
            print("===== Rank Collector finished =====")
        except Exception as e:
            print('Error', e.args)
           
    def run(self):
        self.rank_url()
        self.collector.collect()
        self.downloader.download()
