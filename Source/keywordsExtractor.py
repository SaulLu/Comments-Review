import pandas as pd
import Source.visualizer as visualizer
import spacy
import csv

df_sample_polarity = pd.read_csv('../Data/OrangeDataWithKeywordsAndPolarity.csv')

print(df_sample_polarity['Important'][:40])

text_clean = []