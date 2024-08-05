from configuration import AppConfig
from transformers import AutoTokenizer, AutoModelForSequenceClassification 
from configuration import AppConfig
import torch
import pandas as pd
import os

class GoogleSentimentAnalysis:
    def __init__(self):
        self.config = AppConfig()
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.get_nlp_tokenizer_path())
        self.model = AutoModelForSequenceClassification.from_pretrained(self.config.get_nlp_model_path())
        
        self.perform_sentiment_analysis()


    def get_sentiment_analysis(self, tokenization):
        tokens = self.tokenizer.encode(tokenization, return_tensors='pt')
        results = self.model(tokens)
        return int(torch.argmax(results.logits))+1


    def perform_sentiment_analysis(self):
        # Read data frame 
        df = pd.read_csv(self.config.raw_news_storage_path)
        df['sentiment'] = df['description'].apply(self.get_sentiment_analysis)
        os.makedirs(os.path.dirname(self.config.get_sentiment_news_storage_path()), exist_ok=True)
        df.to_csv(self.config.get_sentiment_news_storage_path(), index=False, header=True)