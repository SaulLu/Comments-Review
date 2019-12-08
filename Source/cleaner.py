#%%
import pandas as pd
import re

#%%
def _clean_verbatim(verbatim:str):
    killpunctuation = str.maketrans('', '', r"-()\"#/@;:<>{}-=~|.?,")
    text = re.sub(r"[-()\"#/@;:<>{}-=~|.?,]","",verbatim)
    return(text)

def clean_comments_colomn(df):
    """
    Only transform the type of the last column for the moment as string
    """
    df2=df
    df2['Verbatim']=df['Verbatim'].astype(str)
    #df2['Verbatim'].apply(_clean_verbatim)
    return(df2)

def clean_moisAnnee_colomn(df):
    """
    Only transform the type of the moisAnnee column to datetime
    """
    df2=df
    try:
        df2['MoisAnnee']=pd.to_datetime(df['MoisAnnee'], format='%Y-%m-%d', errors='raise')
        # do something
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    return(df2)

def clean_Date_reponse_colomn(df):
    """
    Only transform the type of the moisAnnee column to datetime
    """
    df2=df
    try:
        df2['Date de réponse']=pd.to_datetime(df['Date de réponse'], format='%Y-%m-%d', errors='raise')
        # do something
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    return(df2)