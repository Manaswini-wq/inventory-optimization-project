import pandas as pd
import matplotlib.pyplot as plt

def forecast(df):
    df = df.groupby('date')['units_sold'].sum().reset_index()
    df['forecast'] = df['units_sold'].rolling(7).mean()
    return df

def plot_forecast(df):
    plt.plot(df['date'], df['units_sold'], label='Actual')
    plt.plot(df['date'], df['forecast'], label='Forecast', linestyle='--')
    plt.legend()
    plt.title("7-Day Rolling Forecast")
    plt.xlabel("Date")
    plt.ylabel("Units Sold")
    plt.tight_layout()
    plt.savefig('visuals/forecast_plot.png')

if __name__ == "__main__":
    raw = pd.read_csv('data/inventory_data.csv')
    raw['date'] = pd.to_datetime(raw['date'])
    df = forecast(raw)
    plot_forecast(df)
