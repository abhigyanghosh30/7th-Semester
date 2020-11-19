# Number of trees in random forest
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score

train_data_path = 'train.csv'
test_data_path = 'test_sort.csv'

train_data = pd.read_csv(train_data_path, header=None)
test_data = pd.read_csv(test_data_path)

X_train, y_train = train_data.iloc[:, :-1], train_data.iloc[:, -1]
X_test, y_test = test_data.iloc[:, :-1], test_data.iloc[:, -1]
s = StandardScaler()
pca = PCA(n_components=9, whiten=True)
X_train = s.fit_transform(X_train)
X_train = pca.fit_transform(X_train)
X_test = s.transform(X_test)
X_test = pca.transform(X_test)


criterion = ['gini', 'entropy']
class_weight = ['balanced', 'balanced_subsample']
n_estimators = [int(x) for x in np.linspace(start=100, stop=400)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in range(1, 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]  # Create the random grid

random_grid = {'criterion': criterion,
               'class_weight': class_weight,
               'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
print(random_grid)

rf = RandomForestClassifier()
# Random search of parameters, using 3 fold cross validation,
# search across 100 different combinations, and use all available cores
rf_random = RandomizedSearchCV(estimator=rf, param_distributions=random_grid, scoring='f1_micro',
                               verbose=2, n_jobs=-1)  # Fit the random search model
rf_random.fit(X_train, y_train)

print(rf_random.best_params_)


def evaluate(model, test_features, test_labels):
    y_pred = model.predict(test_features)
    f1 = f1_score(y_test, y_pred, average='micro')
    return f1


best_random = rf_random.best_estimator_
random_accuracy = evaluate(best_random, X_test, y_test)

print('Accuracy')

# classifier = SVC(kernel='poly')
# classifier.fit(X_train,y_train)
# y_pred = classifier.predict(X_test)
# precision = precision_score(y_test,y_pred,average='micro')
# recall = recall_score(y_test,y_pred,average='micro')
# accuracy = accuracy_score(y_test,y_pred)
# f1 = f1_score(y_test,y_pred,average='micro')
# print(precision, recall,accuracy,f1)
