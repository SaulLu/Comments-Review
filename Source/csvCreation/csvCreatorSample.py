import pandas as pd

def createCsvSample(path,newPath,sample=0.4):
    df_orange=pd.read_csv(path)
    #Sample extraction of the dataset to help us build our functions
    df_orange_sample=df_orange.sample(frac=sample, replace=True, random_state=1)
    df_orange_sample.to_csv(newPath, index = False)
    
#%%
path='../../Data/OrangeData.csv'
#%%
#Data import
df_orange=pd.read_csv(path)

#%%
#Sample extraction of the dataset to help us build our functions
df_orange_sample=df_orange.sample(frac=0.4, replace=True, random_state=1)
#%%
df_orange_sample.to_csv('../../Data/OrangeDataSample.csv', index = False)
#%%
