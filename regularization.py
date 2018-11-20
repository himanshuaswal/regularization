import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso
train_data = pd.read_csv('data.csv', header = None)
X = train_data.iloc[:,:-1]
y = train_data.iloc[:,-1]
