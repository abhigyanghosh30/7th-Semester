import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import f1_score,precision_score,recall_score,accuracy_score

train_data_path = 'train.csv'  
test_data_path = 'test.csv'  

train_data = pd.read_csv(train_data_path, header=None)

X,y = train_data.iloc[:,:-1], train_data.iloc[:,-1]
s = StandardScaler()
X = s.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 


classifier = KNeighborsClassifier(algorithm = 'ball_tree', leaf_size = 12, n_neighbors = 12, p  = 1, weights = 'distance')
classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)
precision = precision_score(y_test,y_pred,average='micro')
recall = recall_score(y_test,y_pred,average='micro')
accuracy = accuracy_score(y_test,y_pred)
f1 = f1_score(y_test,y_pred,average='micro')
print(precision, recall,accuracy,f1)

classifier = SVC(kernel='poly')
classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)
precision = precision_score(y_test,y_pred,average='micro')
recall = recall_score(y_test,y_pred,average='micro')
accuracy = accuracy_score(y_test,y_pred)
f1 = f1_score(y_test,y_pred,average='micro')
print(precision, recall,accuracy,f1)