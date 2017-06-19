import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from pandas import Series

def analyze_group_differences (df, group, begin, end, plt_title):
    groups = df.loc[:,begin:end].join(df[group]).groupby(group).mean()
    x= [i for i in  groups.iterrows()]
    for i,s in x:
        res = []
        for k,v in s.to_dict().items():
            res.append((i, k, v))
    new_df = pd.DataFrame(data = res, columns = [ 'Gender', 'Title', 'Mean'])
    sns.stripplot(data=new_df, x = 'Mean', y = 'Title', hue= 'Gender', orient='h');
    plt.axvline(x=np.mean(groups.mean()), color='k', lw=4, ls='dashed')
    plt.title(plt_title)
    plt.show()


df = pd.read_csv('responses.csv')
df = df.dropna()
x = df.loc[:, 'Dance':'Opera'].join(df['Gender']).groupby('Gender')
x = x.mean()
analyze_group_differences(df=df, group ='Gender', begin = 'Dance', end = 'Opera', plt_title = 'Музыкальные вкусы')
analyze_group_differences(df=df, group ='Gender', begin = 'Horror', end = 'Action', plt_title = 'Фильмы')
analyze_group_differences(df=df, group ='Gender', begin = 'Horror', end = 'Action', plt_title = 'Фильмы')
analyze_group_differences(df=df, group ='Gender', begin = 'Flying', end = 'Fear of public speaking', plt_title = 'Фобии')
analyze_group_differences(df=df, group ='Gender', begin = 'History', end = 'Pets', plt_title = 'Фобии')
