# -*- coding: utf-8 -*-
"""Project3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1erMcLRPpbDtnA-MBqMzjRaz2kLkTi15L
"""

from itertools import combinations
from collections import defaultdict
from google.colab import drive
drive.mount('/content/drive')


db = set()
header1 = defaultdict(lambda: {'count': 0, 'pointers': []})
minsup = 1000

# data_file = '/content/drive/My Drive/DA-1/fp_test.txt'
data_file = '/content/drive/My Drive/DA-1/project3.txt'

with open(data_file) as f:
    # with open() as f:
    for line in f.readlines():
        attrs = line.strip().split('-1')
        vals = set()
        for val in attrs[:-1]:
            x = val.strip()
            if x not in vals:
                header1[x]['count'] += 1
                vals.add(x)
        db.add(tuple(vals))

header1 = dict(header1)

keys = list(header1.keys())

for item in keys:
    if header1[item]['count'] < minsup:
        header1.pop(item)

keys = list(header1.keys())
# keys are sorted in increasing order of count
keys.sort(key=lambda x: header1[x]['count'], reverse=True)
print(keys)


class Node1:
    def __init__(self, item=None, count=1):
        self.item = item
        self.count = count
        self.children = []
        self.parents = []

    def addChild(self, item, count=1):
        for child in self.children:
            if child.item == item:
                child.count += count
                return child
        new_node = Node1(item=item, count=count)
        header1[item]['pointers'].append(new_node)
        self.children.append(new_node)
        if self.item is not None:
            new_node.parents = self.parents+[self.item]
        return new_node

    def __repr__(self):
        return repr("Item:"+str(self.item)+", Count:"+str(self.count))

    def __str__(self):
        return "Item:"+str(self.item)+", Count:"+str(self.count)


def make_tree1():
    root = Node1()
    for t in db:
        items = list(t)
        items = list(filter(lambda x: x in header1, items))
        items.sort(key=lambda x: header1[x]['count'], reverse=True)
        print(items)
        curr = root
        for item in range(0, len(items)):
            curr = curr.addChild(items[item])
    return root


root = make_tree1()

final = []
keys = list(header1.keys())
keys.sort(key=lambda x: header1[x]['count'], reverse=True)
for item in keys:
    paths = defaultdict(int)
    for pointer in header1[item]['pointers']:
        if pointer.parents != []:
            paths[tuple(pointer.parents)] += pointer.count
    if len(paths) == 0:
        final.append({(item): header1[item]['count']})
        continue
    all_prefixes = set()
    for path in list(paths.keys()):
        for i in range(1, len(path)+1):
            all_prefixes.add(path[:i])
    all_prefixes.add(path)
    common_prefixes = defaultdict(int)
    for prefix in all_prefixes:
        for path in paths:
            if path[:len(prefix)] == prefix:
                common_prefixes[prefix] += paths[path]
    common_prefixes = dict(common_prefixes)
    k = list(common_prefixes.keys())
    for prefix in k:
        if common_prefixes[prefix] < minsup:
            common_prefixes.pop(prefix)
        else:
            final.append({(prefix, item): common_prefixes[prefix]})
    final.append({(item): header1[item]['count']})

print(final)
print(len(final))
