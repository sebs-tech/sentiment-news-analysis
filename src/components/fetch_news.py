import os
import pandas as pd
from google_news_feed import GoogleNewsFeed # type: ignore
from dataclasses import dataclass

@dataclass
class NewsStorageConfig:
    news_storage_path: str=os.path.join('artifacts', 'news_headlines.csv')

class NewsIngestion: 
    def __init__(self):
        self.ingestion_config=NewsStorageConfig()
        self.news_headlines = self.fetch_news()
        self.store_news()

    def fetch_news(self):
        df = pd.DataFrame(GoogleNewsFeed(language='en',country='US').top_headlines())
        return df
    
    def store_news(self):
        os.makedirs(os.path.dirname(self.ingestion_config.news_storage_path), exist_ok=True)
        self.news_headlines['title'].to_csv(self.ingestion_config.news_storage_path, index=False, header=True)

    def storage_path(self):
        return str(self.ingestion_config.news_storage_path)

if __name__=='__main__':
    news=NewsIngestion()
    print(news.storage_path())
    #news.store_news()  

    