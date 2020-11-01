import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, VotingClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.neural_network import MLPClassifier


class Submission():
    def __init__(self, train_data_path, test_data_path):
        self.train_data = pd.read_csv(train_data_path, header=None)
        self.test_data = pd.read_csv(test_data_path)

    def predict(self):
        # Split the training data into x and y
        X_train, y_train = self.train_data.iloc[:,
                                                :-1], self.train_data.iloc[:, -1]

        # Preprocessing
        s = StandardScaler()
        pca = PCA(n_components=9, whiten=True, random_state=101)
        X_train = s.fit_transform(X_train)
        X_train = pca.fit_transform(X_train)
        self.test_data = s.transform(self.test_data)
        self.test_data = pca.transform(self.test_data)

        # classifier = LogisticRegression(C=10**4, penalty='l2') #0.551

        # Train the model
        # clf1 = DecisionTreeClassifier(criterion='gini', max_depth=None, random_state=0)  # 0.607
        # classifier = KNeighborsClassifier(
        #     algorithm='ball_tree', leaf_size=12, n_neighbors=50, p=1, weights='distance')  # 0.673
        classifier = RandomForestClassifier(
            criterion='entropy', max_depth=None,  min_samples_split=2, n_estimators=175)  # 0.696
        # classifier = GradientBoostingClassifier(n_estimators=400, max_depth=10) #0.681
        # classifier = VotingClassifier(estimators=[('knn', clf1), ('dt', clf2), ('rf', clf3)], voting='soft', weights=[0.673, 0.607, 0.696]) # 0.643
        # clf1 = clf1.fit(X_train, y_train)
        # clf2 = clf2.fit(X_train, y_train)
        # clf3 = clf3.fit(X_train, y_train)
        # classifier = AdaBoostClassifier(
        #     base_estimator=clf1, n_estimators=500, learning_rate=0.1, random_state=101)  # 0.609

        # classifier = MLPClassifier(solver='lbfgs', activation='relu',
        #                            alpha=10**-5, hidden_layer_sizes=(50, 25, 10, 5), random_state=1)  # 0.553
        classifier.fit(X_train, y_train)

        # Predict on test set and save the prediction
        submission = classifier.predict(self.test_data)
        submission = pd.DataFrame(submission)
        submission.to_csv('submission.csv', header=['quality'], index=False)
