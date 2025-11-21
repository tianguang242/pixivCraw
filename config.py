from dataclasses import dataclass


@dataclass
class Config:
    cookie: str = ""
    
    user_id: str = ""
    
    store_path="image"
    
    header_u = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }
    
    proxy={'https': '127.0.0.1:7897'}
    
    modle:str="daily"
    # "daily"
    # "weekly"
    # "monthly"
    #  "rookie"  ÐÂÈË
    # "original"  Ô­´´
    # "male"  ÄÐÐÔ
    #  female  Å®ÐÔ
    #  "daily_ai"
    #  "daily_r18"
    #  "weekly_r18" 
    #  "daily_r18_ai"
    #  "male_r18"
    #  "female_r18"

    
    content:str="all"
    # illust
    # manga
    # ugoira
    # novel
    # all

    collecttime="2024-01-19"
    
    relativeday:int=1

    rank:int=49


config=Config()

