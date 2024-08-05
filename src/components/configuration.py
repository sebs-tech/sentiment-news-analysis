###
### configuration.py
###

### Global configuration for the app

import os
from dataclasses import dataclass


@dataclass
class AppConfig:
    ## configure path for incoming raw news storage
    raw_news_storage_path: str=os.path.join('data', 'news_headlines.csv')
    
    ## configure nlp-tokenizer
    
    ## configure nlp 
    nlp_model_name: str="nlptown/bert-base-multilingual-uncased-sentiment"
    
    
    ## configure nlp-tokenizer
    nlp_model_tokenizer: str=os.path.join('nlp', 'tokenizer', nlp_model_name)
    
    ### configure nlp path
    nlp_model_path: str=os.path.join('nlp', 'model', nlp_model_name)
    
    def get_raw_news_storage_path(self) -> str:
        #return path of the storage file
        return self.raw_news_storage_path
    
    def get_nlp_model_name(self) -> str:
        return str(self.nlp_model_name)
    
    def get_nlp_model_path(self) -> str:
        return self.nlp_model_path
    
    def get_nlp_tokenizer_path(self) -> str:
        return str(self.nlp_model_tokenizer)
    
    
if __name__=='__main__':
    news = AppConfig()
    print(news.get_raw_news_storage_path())
    print(news.get_nlp_model_name())
    print(news.get_nlp_model_path())
    print(news.get_nlp_tokenizer_path())