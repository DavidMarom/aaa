import pandas as pd
import string

def clean_tweet_data(df: pd.DataFrame) -> pd.DataFrame:

    # remove rows with NaN in 'Biased' column
    df_clean = df.dropna(subset=['Biased']).copy()

    # keep only relevant columns
    df_clean = df_clean[['Text']]

    # clean the text
    def clean_text(text):
        text = str(text).lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text

    df_clean['Text'] = df_clean['Text'].apply(clean_text)

    return df_clean
