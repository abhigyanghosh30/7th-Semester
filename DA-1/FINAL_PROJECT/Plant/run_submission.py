import pandas as pd
from sklearn.metrics import f1_score
from submission import Submission

sub = Submission('train.csv', 'test.csv')
sub.predict()
# actual = pd.read_csv('test_cheat_sort.csv')
# pred = pd.read_csv('submission.csv')
# print(f1_score(actual.iloc[:, 0], pred.iloc[:, 0], average='micro'))
