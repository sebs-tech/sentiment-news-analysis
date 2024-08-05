###
### utils.py
###

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os


class ClassificationModel:
    def __init__(self):
        self.nlp_model = self.read_model_name()
    
    def read_model_name(self):
        with open('model_config.txt', 'r') as reader:
            lines=reader.readlines()
        return lines[0].strip('\n')
    
    def print_model_name(self): 
        print(self.nlp_model)
    
    
    def fetch_model(self):
        tokenizer = AutoTokenizer.from_pretrained(self.nlp_model)
        tokenizer.save_pretrained(f"cache/tokenizer/{self.nlp_model}")


if __name__=='__main__':
    model = ClassificationModel()
    model.print_model_name()
    #model.print_model()
    #model.fetch_model()
    