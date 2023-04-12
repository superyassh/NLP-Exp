# import required libraries
import pandas as pd 
from textblob import TextBlob
# load sample data 
data = pd.read_csv('sample_data.csv') 
# loop through the data and get the sentiment of each tweet 
for index, row in data.iterrows(): 
    text = row['text']
    sentiment = TextBlob(text).sentiment.polarity
    print("Text: ", text)
    print("Sentiment Score: ", sentiment)
    print("\n")