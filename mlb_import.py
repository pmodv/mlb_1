import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import  numpy as np


# eda for ds1.csv
def check_df(df):

    # let's hunt for missing data

    print('is there a NaN in the table?',df.isnull().values.any())

    # check again
    nan_rows = df[df.isnull().any(1)]
    print('nan rows',nan_rows)
    # solid!

    # check types and examine any non-uniform types (object type, specifically)
    print(df.dtypes)

    # all np.float64
    print(df.head())
    # 0 col looks like index - check with plot linear plot vs df.index

    # yup, 0 col is just index - drop it
    sns.lineplot(y=df.iloc[:,0],x=df.index)
    plt.show()

    df_X = df.iloc[:,1:6]
    print(df_X.head())
    df_y = df.iloc[:,6:10]
    print(df_y.head())
    
    
    
    # list of variables with only > 0 data

    count_cols=[]
    for c in df_X.columns:
        if (df_X[c] >= 0).all():
            print('only non-negatives in this field ', c)
            count_cols.append(c)

    print('non-neg data(e.g. time, etc)', count_cols)

    
    sns.pairplot(df_X)
    plt.title('pairplot of input data')
    plt.show()

    # my guesses:  
    # x1 is uniform
    # x2 is gaussian
    # x3 is beta or maybe t distribution
    # x5 is exponetial 
    # x6 is double-exponetial - centered around 0 
  
   



# only code to execute for runtime proc
try:
    df = pd.read_csv('ds1.csv',sep=',')
except IOError as e:
    print(e)

# for processing-
df_X = df.iloc[:,1:6]
df_y = df.iloc[:,6:10]


# check df and make basic diagnostic plots
# disabled unless explicit diag proc
if __name__ == '__main__':
    check_df(df)

