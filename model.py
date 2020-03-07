import pickle
import pandas as pd
from xgboost import XGBClassifier
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline

URL = 'fin_data.csv'
bank_df = pd.read_csv(URL)

bank_df.drop_duplicates(inplace=True)
bank_df.dropna(inplace=True)
bank_df.drop('degree', axis=1, inplace=True)
bank_df = bank_df[bank_df['marital_status'] > 0]
bank_df['education_level'] = bank_df['education_level'].apply(lambda x: 0 if x>3 else x)
bank_df.reset_index(drop=True, inplace=True)


X = bank_df.drop('default_payment_next_month', axis=1)
y = bank_df['default_payment_next_month'] 

model=Pipeline([('preprocessor', MinMaxScaler()), 
	('classifier', XGBClassifier(scale_pos_weight=4, tree_method='hist', grow_policy='lossguide', max_depth=3, n_estimators=100))])

model.fit(X, y)


pickle.dump(model, open('model.pkl','wb'))





