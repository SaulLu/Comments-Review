import pandas as pd
import spacy
import csv

df_orange=pd.read_csv('../../Data/OrangeData.csv')
df_sample_polarity = pd.read_csv('../../Data/OrangeDataWithPolaritySample.csv')

nlp = spacy.load('fr_core_news_md')
list_types = ['VERB', 'NOUN', 'ADJ']

def compute_important_word(string, i) :
    if (i%1000==0):
        print(i)
    important_words = []
    doc = nlp(string)
    for word in doc :
        if word.pos_ in list_types :
            important_words.append(word.text)
    return important_words


df_test = df_sample_polarity.copy()
df_test['Important'] = [compute_important_word(str(comment), i) for i,comment in enumerate(df_test['Verbatim'])]

df_test.to_csv('../../Data/OrangeDataWithKeywordsAndPolarity.csv', index = False)

print('Done')
