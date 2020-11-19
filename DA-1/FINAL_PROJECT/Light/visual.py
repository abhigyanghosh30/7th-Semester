import os
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot as plt

# Train and test data paths will be available as env variables during evaluation
TRAIN_DATA_PATH = os.getenv("TRAIN_DATA_PATH", default='./train.csv')
TEST_DATA_PATH = os.getenv("TEST_DATA_PATH", default='./test.csv')

train_data = pd.read_csv(TRAIN_DATA_PATH)
X_train, y_train = train_data.iloc[:, :-1], train_data.iloc[:, -1]

pca = PCA(n_components=2)
pca.fit_transform(X_train)
plt.scatter(X_train.iloc[:, 0], X_train.iloc[:, 1])
plt.show()
