# import required libraries
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# download necessary resources
nltk.download('vader_lexicon')

# load the texts
texts = ["I love working with Python!", 
         "The weather is terrible today.",
         "This movie is absolutely amazing!",
         "I don't like this restaurant at all."]

# create a SentimentIntensityAnalyzer object
analyzer = SentimentIntensityAnalyzer()

# loop through the texts and get the sentiment of each text
for text in texts:
    scores = analyzer.polarity_scores(text)
    print("\n")
    if scores['compound'] > 0:
        print("Text: ", text)
        print("Positive Sentiment")
        print("Sentiment Score: ", scores['compound'])
    elif scores['compound'] < 0:
        print("Text: ", text)
        print("Negative Sentiment")
        print("Sentiment Score: ", scores['compound'])
    else:
        print("Text: ", text)
        print("Neutral Sentiment")
        print("Sentiment Score: ", scores['compound'])


