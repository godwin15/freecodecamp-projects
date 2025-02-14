import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12,6))
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], label='Data', alpha=0.5)
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.title('Sea Level Change Over Time')

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, slope * years_extended + intercept, 'r', label='Best Fit (1880-2050)')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope, intercept, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(2000, 2051))
    plt.plot(years_extended, slope * years_extended + intercept, 'r', label='Best Fit (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()