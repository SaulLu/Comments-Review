#%%
import pandas as pd


# %%
df_orange=pd.read_excel("Verbatim DEF E&ProPME_2017-2019_EJardat_oct19.xlsx")

# %%
df_orange_sample=df_orange.sample(frac=0.4, replace=True, random_state=1)

# %%
df_orange.head()


# %%
df_orange_sample.head()



# %%
df_orange_sample.describe()

# %%
df_orange_sample.dtypes

# %%
df_orange_sample["Verbatim"]= df_orange_sample["Verbatim"].astype(str) 


# %%
# %%
from textblob import TextBlob

# %%
sentiment_scores_tb = [round(TextBlob(article).sentiment.polarity, 3) for article in df_orange_sample['Verbatim']]
sentiment_category_tb = ['positive' if score > 0 
                             else 'negative' if score < 0 
                                 else 'neutral' 
                                     for score in sentiment_scores_tb]

# %%
print(sentiment_scores_tb)
#%%
from textblob_fr import PatternTagger, PatternAnalyzer

# %%
sentiment_scores_tb = [round(TextBlob(article, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer()).sentiment[0], 3) for article in df_orange_sample['Verbatim']]
sentiment_category_tb = ['positive' if score > 0 
                             else 'negative' if score < 0 
                                 else 'neutral' 
                                     for score in sentiment_scores_tb]

# %%
print(sentiment_category_tb)

# %%
count_positive=0
count_negative=0
count_neutral=0
count_total=len(sentiment_category_tb)
for avis in sentiment_category_tb:
    if avis =='positive':
        count_positive+=1
    if avis =='negative':
        count_negative+=1
    else :
        count_neutral+=1

pourcent_positive=count_positive/count_total*100
print(f"Nombre d'utilisateurs contents {pourcent_positive}%")


# %%
