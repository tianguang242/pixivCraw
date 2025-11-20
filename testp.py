import os
import requests
from config import config 
import tqdm

from rank import Rank
os.makedirs(config.store_path, exist_ok=True)
app=Rank(200)
app.run()
"""
   art_work_json=[{
        'author':i['user_name'],
        'pid':i['illust_id'],
        'tittle':i['title']
        }
         for i in art_work]
    filepath=os.path.join(config.store_path,"a.json")
    with open(filepath,'w',encoding='utf-8') as f:
        f.write(json.dumps(art_work_json, indent=4, ensure_ascii=False)
"""