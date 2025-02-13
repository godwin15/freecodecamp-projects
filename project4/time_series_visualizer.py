import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
np.float = float
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col= 'date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    # Create figure and plot the line chart
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df["value"], color="red", linewidth=1)

    # Set title and labels
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month
    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    # Draw bar plot
    fig = df_bar.plot(kind="bar", figsize=(8, 6)).figure

    # Set labels and title
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.title("Average Daily Page Views per Month")
    plt.legend(
        title="Months",
        labels=[
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
    )

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    # order month well
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, axes = plt.subplots(1,2,figsize=(15,6))

    #year wise box plots
    sns.boxplot(x='year', y='value', data=df_box, palette="Set1", ax= axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    #month wise box plots
    sns.boxplot(x='month', y='value', data=df_box, order= month_order, palette="Set1", ax= axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
