import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
 
def encode_onehot(df, cols):
    """
    One-hot encoding is applied to columns specified in a pandas DataFrame.
    
    Modified from: https://gist.github.com/kljensen/5452382
    
    Details:
    
    http://en.wikipedia.org/wiki/One-hot
    http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html
    
    @param df pandas DataFrame
    @param cols a list of columns to encode
    @return a DataFrame with one-hot encoding
    """
    vec = DictVectorizer()
    
    vec_data = pd.DataFrame(vec.fit_transform(df[cols].to_dict(outtype='records')).toarray())
    vec_data.columns = vec.get_feature_names()
    vec_data.index = df.index
    
    df = df.drop(cols, axis=1)
    df = df.join(vec_data)
    return df

data = pd.read_csv('../input/train.csv')
print('load in data: train.csv')

data.drop('id',axis=1,inplace=True)
print(data.shape)

row, col = data.shape
feature_cols = list(data.columns[0:-1])
target_cols = data.columns[-1]

print('normalizing target label')
data[target_cols] = np.log1p(data[target_cols])
print('getting labels')

cat_col = 115
labels= []


for i in range(0,cat_col):
    train = data[feature_cols[i]].unique()
    labels.append(list(set(train)))
    
 
