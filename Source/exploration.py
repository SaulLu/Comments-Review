
#%%
import pandas as pd
import datetime

#%%
df_orange=pd.read_csv('./Data/OrangeData.csv')

#%%
#Sample extraction of the dataset to help us build our functions
df_orange_sample=df_orange.sample(frac=0.4, replace=True, random_state=1).reset_index(drop=True)

#%%
#Data exploration
# %%
df_orange_sample.columns

#%%

#%%
df_orange_sample.head()

# %%
df_orange_sample.describe()

# %%
df_orange_sample.dtypes

# %%
df_orange_sample["Libellé de la question du Verbatim"].unique()

# %%
for moisAnnee in df_orange_sample["MoisAnnee"]:
    date_text=moisAnnee
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        print("ok")
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

# %%
