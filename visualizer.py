import pandas as pandas
import matplotlib.pyplot as plt
import seaborn as sns

def count_number_sondage(dataframe):
    return(dataframe[["Verbatim", "Nom du sondage"]].groupby("Nom du sondage").agg("count").rename(columns={
        "Verbatim": "count"}))

def count_polarity_global(dataframe_with_polarity):
    return(dataframe_with_polarity[["Verbatim", "Sentiment Polarity"]].groupby("Sentiment Polarity").agg("count").rename(columns={
        "Verbatim": "count"}).reset_index())

def count_polarity_groupby(dataframe_with_polarity, name_column ):
    return(dataframe_with_polarity[["Verbatim", "Sentiment Polarity",
                            name_column]].groupby([
                                name_column, "Sentiment Polarity"
                            ]).agg("count").rename(columns={
                                "Verbatim": "count"
                            }).reset_index())


def plot_pie_chart(df, column_name:str, size=(6,8)):
    df.plot.pie(y=column_name, figsize=size)

def plot_bar(df, figsize=(8,4)):
    fig, ax = plt.subplots(figsize=figsize)
    df.plot.bar(ax=ax)
    sns.despine()

def plot_polarity_groupby(df, name_column, figsize=(8,4)):
    fig, ax = plt.subplots(figsize=figsize)
    sns.barplot(x="count",
                hue="Sentiment Polarity",
                y=name_column,
                data=df,
                ax=ax)
    sns.despine()



def count_polarity_libelle(dataframe_with_polarity):
    return(count_polarity_groupby(dataframe_with_polarity, "Libellé de la question du Verbatim" ))

def plot_polarity_groupby_libelle(df, figsize=(8,4)):
    plot_polarity_groupby(df, "Libellé de la question du Verbatim", figsize)

def count_polarity_sondage(dataframe_with_polarity):
    return(count_polarity_groupby(dataframe_with_polarity, "Nom du sondage" ))


def plot_polarity_groupby_sondage(df, figsize=(8,4)):
    plot_polarity_groupby(df, "Nom du sondage" , figsize)