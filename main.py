#%%
import pandas as pd
import cleaner
import polarizer
import visualizer
import matplotlib.pyplot as plt
import seaborn as sns

#%%
#set path : CSV file in Data folder
path='./Data/OrangeData.csv'
#%%
#Data import
df_orange=pd.read_csv(path)

#%%
#Sample extraction of the dataset to help us build our functions
df_orange_sample=df_orange.sample(frac=0.4, replace=True, random_state=1)
# %%
df_orange_sample.head()
#%%
df_orange_sample_clean=cleaner.clean_comments_colomn(df_orange_sample)

# %%
df_orange_sample_clean=cleaner.clean_moisAnnee_colomn(df_orange_sample_clean)
# %%
df_orange_sample.head()
#%%
sentiment_category_tb=polarizer.polarizer_text_blob_french(df_orange_sample_clean['Verbatim'])

#%%
polarizer.add_polarised_column(df_orange_sample_clean,sentiment_category_tb)

#%%
df_orange_sample_clean.head()

#%%
#Download
df_orange_sample_clean.to_csv('./Data/OrangeDataWithPolaritySample.csv', index = False)



# %%
