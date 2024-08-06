# Google News Sentiment Analysis 

Google-news-sa is an application that uses Natural Language Processing (NLP) to analyze the 
sentiment of Google News headlines. For the sentiment analysis the app uses *'nlptown/bert-base-multilingual-uncased-sentiment'* model and tokenizer from Huggingface.com


## How it works
The application produces a list of headlines, with a button below warning the user about the sentimental intepretation of the headline. 
The categorization falls basically in 3 categories: 
* Bad
* Neutral
* Good / ok

By clicking on the button bellow the headline, the user can read the full article. 


## How to install 

```
https://github.com/sebs-tech/sentiment-news-analysis.git
```

```
cd sentiment-news-analysis
pip install -r requirements.txt
```

## Docker 
The docker is available at dockerhub
```
https://hub.docker.com/r/sebstech/google-news-sa
```

Run the docker with:
```
docker run -p 8080:8080 google-news-sa
```


## Credits 
[Alexey Pelykh](https://alexey-pelykh.com/) for constant support on software architecture / engineering.


## License
Unknown yet. 
