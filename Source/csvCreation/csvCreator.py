import pandas as pd
#%%
import os 
print(os.getcwd())
#%%

def csvCreation(path, path_csv):
    df_orange=pd.read_excel(path)
    df_orange.to_csv(path_csv, index = False)

#set path
#Excel file in Data folder
path="../../Data/Copie de Verbatim 2019 sondages DEF Q1.xlsx" #Path to run the code from Big Data folder
path_csv='../../Data/OrangeData.csv'

#Data import
df_orange=pd.read_excel(path)
#%%
#CSV file creation
df_orange.to_csv('../../Data/OrangeData.csv', index = False)
