import pandas as pd

def preliminary_data(df):
    if not pd.api.types.is_datetime64_any_dtype(df.index):
        df.index = pd.to_datetime(df.index)
    df = df.asfreq('QS')
    df.columns = ['GDP']
    df['GDP'] = pd.to_numeric(df['GDP'], errors='coerce')
    df=df.dropna()
    return df