#%%
import pandas as pd
import Source.cleaner as cleaner
import Source.polarizer as polarizer
import Source.visualizer as visualizer
import matplotlib.pyplot as plt
import seaborn as sns
import csvCreator

def createTreatCsvDateReponse(path,newpath):
    df_orange_sample=pd.read_csv(path)
    df_orange_sample_clean=cleaner.clean_comments_colomn(df_orange_sample)
    df_orange_sample_clean=cleaner.clean_Date_reponse_colomn(df_orange_sample_clean)
    sentiment_category_tb=polarizer.polarizer_text_blob_french(df_orange_sample_clean['Verbatim'])
    polarizer.add_polarised_column(df_orange_sample_clean,sentiment_category_tb)
    #Download
    df_orange_sample_clean.to_csv(newpath, index = False)

def createTreatCsv(path,newpath):
    df_orange_sample=pd.read_csv(path)
    df_orange_sample_clean=cleaner.clean_comments_colomn(df_orange_sample)
    df_orange_sample_clean=cleaner.clean_moisAnnee_colomn(df_orange_sample_clean)
    sentiment_category_tb=polarizer.polarizer_text_blob_french(df_orange_sample_clean['Verbatim'])
    polarizer.add_polarised_column(df_orange_sample_clean,sentiment_category_tb)
    #Download
    df_orange_sample_clean.to_csv(newpath, index = False)

#%%
#set path : CSV file in Data folders
path='./Data/OrangeDataSample.csv'
#%%
#Data import
df_orange_sample=pd.read_csv(path)
#%%
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
