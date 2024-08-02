import os
import pandas as pd
from google_news_feed import GoogleNewsFeed
from dataclasses import dataclass

@dataclass
class NewsStorageConfig:
    news_storage_path: str=os.path.join('../artifacts', 'news_headlines.txt')


class NewsIngestion: 
    def __init__(self):
        self.ingestion_config=NewsStorageConfig()
        self.news = pd.DataFrame(GoogleNewsFeed(language='en',country='US').top_headlines())

    def news_filter_today():
        '''
        filter out only today published news
        '''
        ## Convert dateTime of post to date format 
        ## Filter by today's date 
        pass


    def news_ingestion(self):
        '''
        save news to a file
        '''
        try:
            print(self.ingestion_config)
            #os.makedirs(self.ingestion_config, exist_ok=True)
        except:
            pass 
    
    def print_news(self):
        print(self.news['pubDate'])
        



if __name__=='__main__':
    print('fetch news')
    news = NewsIngestion()
    news.print_news()
    #news.news_ingestion()
    