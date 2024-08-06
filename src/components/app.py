###
###  app.py
###
import streamlit as st
import subprocess
import pandas as pd
import torch

from google_news import GoogleNews
from configuration import AppConfig
from google_sentiment_analysis import GoogleSentimentAnalysis


def fetch_google_news():
    try:
    
        process = subprocess.run(
            ['python', 'src/components/google_news.py'],
            check=True,
            capture_output=True,
            text=True
        )
    
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
 

if __name__=='__main__':
    config = AppConfig()
    # Fetch and store google news
    fetch_google_news()

    gsa = GoogleSentimentAnalysis()
    
    st.title('Google News Sentiment Analysis')
    st.write("##### Here is a list of Google news with sentiment analysis")
    st.write(" ")
    
    #st.dataframe(df)
    
    df = pd.read_csv(config.sentiment_news_storage_path)
    
    for each in range(0, df.shape[0]):
        if (df.iloc[each]['sentiment'] == 1):
            st.write(f":red[{df.iloc[each]['title']}]")
            st.link_button("Caution: Negative sentiment", str(df.iloc[each]['link']))
            st.write("---")
            
        if (df.iloc[each]['sentiment'] == 2):
            st.write(f":red[{df.iloc[each]['title']}]")
            st.link_button("Caution: Barely acceptable sentiment", str(df.iloc[each]['link']))
            st.write("---")

        if (df.iloc[each]['sentiment'] == 3):
            st.write(f":orange[{df.iloc[each]['title']}]")
            st.link_button("Neutral news sentiment", str(df.iloc[each]['link']))
            st.write("---")
            
        if (df.iloc[each]['sentiment'] == 4):
            st.write(f":green[{df.iloc[each]['title']}]")
            st.link_button("Otimistic news sentiment", str(df.iloc[each]['link']))
            st.write("---")
            
        if (df.iloc[each]['sentiment'] == 5):
            st.write(f":green[{df.iloc[each]['title']}]")
            st.link_button("Good news sentiment", str(df.iloc[each]['link']))
            st.write("---")