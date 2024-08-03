from fetch_news import NewsIngestion
import pandas as pd

class SentimentAnalysis():
    def __init__(self):
        news = NewsIngestion()
        self.news_storage_path = news.storage_path()
        self.news_headlines = self.read_news_headlines()
        
    def read_news_headlines(self):
        df = pd.read_csv(self.news_storage_path)
        return df['title'].tolist()
    
    def news_sentiment_analysis(self): 
        pass

    def show_news_headlines(self):
        for each in self.news_headlines:
            print(each)

if __name__=='__main__':
    sa = SentimentAnalysis()
    #print(sa.news_sentiment_analysis())
    #sa.news_sentiment_analysis()
    sa.show_news_headlines()
    

    