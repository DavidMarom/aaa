import pandas as pd
import string

def clean_tweet_data(df: pd.DataFrame) -> pd.DataFrame:

    # keep only relevant columns
    df_clean = df[['Text', 'Biased']].copy()

    # remove rows with NaN in 'Biased' column
    df_clean = df_clean.dropna(subset=['Biased'])

    # clean the text
    def clean_text(text):
        text = str(text).lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text

    df_clean['Text'] = df_clean['Text'].apply(clean_text)

    return df_clean
