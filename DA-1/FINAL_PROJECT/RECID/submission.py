import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier


# Train and test data paths will be available as env variables during evaluation
TRAIN_DATA_PATH = os.getenv("TRAIN_DATA_PATH", default='./train.csv')
TEST_DATA_PATH = os.getenv("TEST_DATA_PATH", default='./test.csv')

# Prepare the training data
train_data = pd.read_csv(TRAIN_DATA_PATH)
X_train, y_train = train_data.iloc[:, :-1], train_data.iloc[:, -1]
# X_train['average'] = X_train.mean(axis=1)


# Train the model
sc = StandardScaler()
pca = PCA(n_components=10)
pca.fit_transform(X_train)
sc.fit_transform(X_train)
classifier = RandomForestClassifier(n_estimators=1000)
classifier.fit(X_train, y_train)

# Predict on the test set
test_data = pd.read_csv(TEST_DATA_PATH)
pca.transform(test_data)
sc.transform(test_data)
# test_data['average'] = test_data.mean(axis=1)
submission = classifier.predict(test_data)
submission = pd.DataFrame(submission)

# Export the prediction as submission.csv
submission.to_csv('submission.csv', header=['class'], index=False)
