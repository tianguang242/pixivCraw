from dataclasses import dataclass


@dataclass
class Config:
    cookie: str = "first_visit_datetime_pc=2025-11-17%2014%3A59%3A51; cc1=2025-11-17%2014%3A59%3A51; p_ab_id=4; p_ab_id_2=8; p_ab_d_id=337097178; yuid_b=OEA2AZA; _gcl_au=1.1.1022476657.1763359214; _ga=GA1.1.1942460275.1763359214; __utmc=235335808; __utmz=235335808.1763359214.1.1.utmcsr=pixiv.help|utmccn=(referral)|utmcmd=referral|utmcct=/; PHPSESSID=103855241_tFsoziGbTYn7GbH8ZWZQtwwsCZT59udh; device_token=5a3ab3e3e3625ea46ebc05c2e9c05920; c_type=35; privacy_policy_agreement=0; privacy_policy_notification=0; a_type=0; b_type=1; _ga_MZ1NL4PHH0=GS2.1.s1763359229$o1$g1$t1763359334$j60$l0$h0; cto_bundle=0L6j018wenJnVVRiMWxOTjlqUkNKZXlvdzYlMkY3V1NRJTJGRndsdlVjNU5RYkZlZnVDTSUyQlh1VXk3Q1YlMkJ4S1F5JTJGdGJPYkNHekRaQ1VwbHRJTTIlMkZYbmw5JTJCdUh3M2VjdFJtZkJwQUdXeDklMkZSNmllR3BPZVpZZ3Z5T1FNYVVUWWlzMGg2NiUyRmJTZXMyUm5GczlzSTZKZTZSV3FNc3RXQ2clM0QlM0Q; __bnc_pfpuid__=16vr-NaUV2miSrB; _im_vid=01KA86K63K84TCR57RT7RH322K; __utmv=235335808.|2=login%20ever=no=1^3=plan=normal=1^5=gender=male=1^9=p_ab_id=4=1^10=p_ab_id_2=8=1; __utmt=1; __utma=235335808.1942460275.1763359214.1763367635.1763367635.4; __utmb=235335808.7.10.1763367635; _ga_75BBYNYN9J=GS2.1.s1763370156$o4$g1$t1763370512$j60$l0$h0"
    
    user_id: str = "103855241"
    
    store_path="image"
    
    header_u = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }
    
    proxy={'https': '127.0.0.1:7897'}
    
    modle:str="daily"
    # "daily"
    # "weekly"
    # "monthly"
    #  "rookie"  新人
    # "original"  原创
    # "male"  男性
    #  female  女性
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
