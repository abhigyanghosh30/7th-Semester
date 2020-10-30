import pandas as pd
import numpy as np
from sklearn.svm import SVC 
from sklearn.preprocessing import StandardScaler

class Submission():
    def __init__(self, train_data_path, test_data_path):
        self.train_data = pd.read_csv(train_data_path, header=None)
        self.test_data = pd.read_csv(test_data_path)

    def predict(self):
        # Split the training data into x and y
        X_train,y_train = self.train_data.iloc[:,:-1], self.train_data.iloc[:,-1]
        
        # Preprocessing
        s = StandardScaler()
        X_train = s.fit_transform(X_train)
        self.test_data = s.transform(self.test_data)

        # Train the model
        classifier = SVC()
        classifier.fit(X_train, y_train)
        
        # Predict on test set and save the prediction
        submission = classifier.predict(self.test_data)
        submission = pd.DataFrame(submission)
        submission.to_csv('submission.csv',header=['quality'],index=False)
