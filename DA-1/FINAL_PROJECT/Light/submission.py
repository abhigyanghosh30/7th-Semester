import os
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# Train and test data paths will be available as env variables during evaluation
TRAIN_DATA_PATH = os.getenv("TRAIN_DATA_PATH", default='./train.csv')
TEST_DATA_PATH = os.getenv("TEST_DATA_PATH", default='./test.csv')

# Prepare the training data
train_data = pd.read_csv(TRAIN_DATA_PATH)
X_train, y_train = train_data.iloc[:, :-1], train_data.iloc[:, -1]
# X_train['average'] = X_train.mean(axis=1)


# Train the model
# classifier = SVC(gamma='auto')
models = [('rf', RandomForestClassifier(n_estimators=1000, random_state=42)),
          ('svr', DecisionTreeClassifier())]

classifier = StackingClassifier(
    estimators=models, final_estimator=SVC())
classifier.fit(X_train, y_train)

# Predict on the test set
test_data = pd.read_csv(TEST_DATA_PATH)
# test_data['average'] = test_data.mean(axis=1)
submission = classifier.predict(test_data)
submission = pd.DataFrame(submission)

# Export the prediction as submission.csv
submission.to_csv('submission.csv', header=['class'], index=False)
