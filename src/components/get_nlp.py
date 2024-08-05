###
### get_nlp.py
###

### Downloads and stores the NLP model depending on the AppConfig

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from configuration import AppConfig


if __name__=='__main__':
    news = AppConfig()
    
    # Fetch NLP tokenizer
    tokenizer = AutoTokenizer.from_pretrained(news.get_nlp_model_name())
    tokenizer.save_pretrained(news.get_nlp_tokenizer_path())
    
    # Fetch NLP model
    model = AutoModelForSequenceClassification.from_pretrained(news.get_nlp_model_name())
    model.save_pretrained(news.get_nlp_model_path())