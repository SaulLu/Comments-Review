import pandas as pd

#set path
#Excel file in Data folder
path="./Data/Verbatim DEF E&ProPME_2017-2019_EJardat_oct19.xlsx" #Path to run the code from Big Data folder
path_csv='./Data/OrangeData.csv'

#Data import
df_orange=pd.read_excel(path)

#CSV file creation
df_orange.to_csv('./Data/OrangeData.csv', index = False)
