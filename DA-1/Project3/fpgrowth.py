import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
data_file='project3.txt'
dataset = []
with open(data_file) as f:
    for line in f.readlines():
        attrs = line.strip().split('-1')
        vals = []
        for val in  attrs[:-1]:
            x = val.strip()
            vals.append(x)
        dataset.append(list(vals))
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
print(fpgrowth(df, min_support=0.0001))
