import pandas as pd

def clean_inventory_data(path):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna()
    return df

if __name__ == "__main__":
    df = clean_inventory_data('data/inventory_data.csv')
    print(df.head())
