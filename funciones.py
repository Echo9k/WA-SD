import pandas as pd


def downcaster(df):
    fcols = df.select_dtypes('float').columns
    icols = df.select_dtypes('integer').columns

    df[fcols] = df[fcols].apply(pd.to_numeric, downcast='float')
    df[icols] = df[icols].apply(pd.to_numeric, downcast='integer')
    return df

def to_categorical(df, columns):
    for col in columns:
        df[col] = pd.Categorical(df[col])
    return df