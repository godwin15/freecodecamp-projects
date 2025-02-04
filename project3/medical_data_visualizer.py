import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = np.where(df['weight']/((df['height']/100)**2) > 25, 1, 0)

# 3
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)
df['cholesterol'] = np.where(df['cholesterol']==1, 0, 1)


# 4
def draw_cat_plot():
    # 5
    df_cat = df[['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']]


    # 6
    df_cat = pd.melt(df_cat, id_vars=['cardio'],var_name='feature', value_name='value')
    

    # 7
    df_cat_grouped = df_cat.groupby(['cardio', 'feature', 'value']).size().reset_index(name='count')
    df_cat_grouped = df_cat_grouped.rename(columns={'feature': 'variable', 'count': 'total'})

    # 8
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat_grouped, kind='bar').figure

    # 9
    fig.savefig('catplot.png')
    return fig



# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &  # Diastolic <= Systolic
        (df['height'] >= df['height'].quantile(0.025)) &  # Height >= 2.5th percentile
        (df['height'] <= df['height'].quantile(0.975)) &  # Height <= 97.5th percentile
        (df['weight'] >= df['weight'].quantile(0.025)) &  # Weight >= 2.5th percentile
        (df['weight'] <= df['weight'].quantile(0.975))   # Weight <= 97.5th percentile
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    plt.figure().clear()
    fig, ax = plt.subplots(figsize=(10, 8))
    

    # 15
    sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', fmt=".1f", ax=ax)
    #ax.set_title("Correlation Matrix (Upper Triangle)")


    # 16
    fig.savefig('heatmap.png')
    return fig
