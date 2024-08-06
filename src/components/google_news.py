###
### google_news.py
###

### Fetch anb ingest google news 
import os
import pandas as pd
from google_news_feed import GoogleNewsFeed
from configuration import AppConfig

class GoogleNews:
    def __init__(self):
        self.config = AppConfig()
        self.store_google_news()
    
    
    def fetch_google_news(self):
        df = pd.DataFrame(GoogleNewsFeed(language='en',country='US').top_headlines())
        return df
    
    
    def store_google_news(self):
        os.makedirs(os.path.dirname(self.config.get_raw_news_storage_path()), exist_ok=True)
        self.fetch_google_news().to_csv(self.config.get_raw_news_storage_path(), index=False, header=True)
        

if __name__=='__main__':
    google_news = GoogleNews()
    