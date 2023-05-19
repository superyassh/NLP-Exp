import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import SentimentOptions, Features, EntitiesOptions, KeywordsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Set up the Natural Language Understanding client
authenticator = IAMAuthenticator('IBM CLOUD API KEY')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-09-01',
    authenticator=authenticator
)
natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/9780d686-9ed1-4800-87c1-c7f1abd93cfa')

# Analyze the sentiment of a text document
text = input("Write the text for sentiment ananlysis: ")
response = natural_language_understanding.analyze(
    text=text,
    features=Features(sentiment=SentimentOptions())
).get_result()

# Print the sentiment score and label
sentiment_score = response['sentiment']['document']['score']
sentiment_label = response['sentiment']['document']['label']
print('Sentiment score:', sentiment_score)
print('Sentiment label:', sentiment_label)
