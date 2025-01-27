import numpy as np
import pandas as pd

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

def highest_gdp(URL):
    tables = pd.read_html(URL)
    df = pd.DataFrame(tables[3])
    df.columns = range(df.shape[1])   #changes title of columns to numbers

    df = df[[0,2]]
    df = df.iloc[1:11,:]

    df.columns = ['Country','GDP (Million USD)']
    
    df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)   #column's datatype is converted to int
    df['GDP (Million USD)'] = (df[['GDP (Million USD)']]/1000)  #converts to billion USD
    df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2)  #rounds off to 2 decimal places
    df.rename(columns = {'GDP (Million USD)' : 'GDP (Billion USD)'})

    df.to_csv('largest economies.csv')

    print(df)

highest_gdp(URL)
