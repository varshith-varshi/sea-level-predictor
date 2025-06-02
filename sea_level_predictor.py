import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', color='blue')

    # 3. Line of best fit for all data
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = pd.Series(range(1880, 2051))
    y_all = res_all.slope * x_all + res_all.intercept
    plt.plot(x_all, y_all, label='Best Fit Line 1880-2050', color='red')

    # 4. Line of best fit from year 2000 onward
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_recent.slope * x_recent + res_recent.intercept
    plt.plot(x_recent, y_recent, label='Best Fit Line 2000-2050', color='green')

    # 5. Plot settings
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # 6. Save and return the figure
    plt.grid(True)
    fig = plt.gcf()
    fig.savefig('sea_level_plot.png')
    return fig
