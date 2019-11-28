from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

def polarizer_text_blob_english(df_Verbatim):
    """
    Method which generate a list of categories of sentiments (neutral, positive, negative) given a dataframe of textual comments in english
    Input : a dataframe with only one column of strings
    Output : a list of strings
    """
    sentiment_scores_tb = [round(TextBlob(article).sentiment.polarity, 3) for article in df_Verbatim]
    sentiment_category_tb = ['positive' if score > 0 
                                else 'negative' if score < 0 
                                    else 'neutral' 
                                        for score in sentiment_scores_tb]
    return(sentiment_category_tb)

def polarizer_text_blob_french(df_Verbatim):
    """
    Method which generate a list of categories of sentiments (neutral, positive, negative) given a dataframe of textual comments in french
    Input : a dataframe with only one column of strings
    Output : a list of strings
    """
    sentiment_scores_tb = [round(TextBlob(article, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer()).sentiment[0], 3) for article in df_Verbatim]
    sentiment_category_tb = ['positive' if score > 0 
                             else 'negative' if score < 0 
                                 else 'neutral' 
                                     for score in sentiment_scores_tb]
    return(sentiment_category_tb)

def add_polarised_column(dataframe_clean,list_polarity):
    """
    Method which add a new column to the dataframe
    Input : a dataframe 
    Output : a dataframe with a new column 'Sentiment Polarity' filled with the data in list_polarity
    """
    dataframe_clean['Sentiment Polarity']=list_polarity

