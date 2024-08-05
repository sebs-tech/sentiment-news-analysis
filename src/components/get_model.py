###
### get_model.py
###

### Downloads and stores the NLP model 

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name="nlptown/bert-base-multilingual-uncased-sentiment"

'''
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.save_pretrained(f"cache/tokenizer/{model_name}")

model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.save_pretrained(f"cache/model/{model_name}")
'''

tokenizer = AutoTokenizer.from_pretrained(f"cache/tokenizer/{model_name}")
model = AutoModelForSequenceClassification.from_pretrained(f"cache/model/{model_name}")


tokens = tokenizer.encode("Tesla, Charles Schwab — and now Chevron: Texas is having a moment.", return_tensors='pt')
result = model(tokens)


print(torch.argmax(result.logits))

#sentiment_task = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, device='cuda')
#sentiment_task("Covid cases are increasing fast!")

''