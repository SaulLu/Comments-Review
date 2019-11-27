#%%
import pandas as pd
import cleaner
import polarizer
import visualizer
import matplotlib.pyplot as plt
import seaborn as sns

#%%
#set path : CSV file in Data folder
path='./Data/OrangeDataWithPolaritySample.csv'
#%%
#Data import
df_orange_sample_clean=pd.read_csv(path)

# %%
df_sentiment_by_libelle=visualizer.count_polarity_libelle(df_orange_sample_clean)

# %%
visualizer.plot_polarity_groupby_libelle(df_sentiment_by_libelle, figsize=(8,12))

#%%
df_sentiment_by_sondage=visualizer.count_polarity_sondage(df_orange_sample_clean)

# %%
visualizer.plot_polarity_groupby_sondage(df_sentiment_by_sondage, figsize=(8,12))
# %%
visualizer.plot_pie_chart(visualizer.count_number_sondage(
    df_orange_sample_clean),'Nom du sondage')

# %%
