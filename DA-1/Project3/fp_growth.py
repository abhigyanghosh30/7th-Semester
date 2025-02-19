# -*- coding: utf-8 -*-
# """TD_FP_Growth.ipynb
#
# Automatically generated by Colaboratory.
#
# Original file is located at
#     https://colab.research.google.com/drive/18_570ikTQRLHV-J0xay5LaWz3WDv8wEN
# """
#
# from google.colab import drive
# drive.mount('/content/drive')

from collections import defaultdict
from itertools import combinations
import sys
import time

# data_file = '/content/drive/My Drive/DA-1/fp_test.txt'
# data_file = '/content/drive/My Drive/DA-1/project3.txt'
data_file = sys.argv[1]
minsup = int(sys.argv[2])


def TD():
    header = defaultdict(lambda: {'count': 0, 'pointers': []})
    db = set()
    with open(data_file) as f:
        for line in f.readlines():
            attrs = line.strip().split('-1')
            vals = []
            for val in attrs[:-1]:
                x = val.strip()
                if x not in vals:
                    vals.append(x)
                    header[x]['count'] += 1
            db.add(tuple(vals))

    header = dict(header)
    keys = list(header.keys())

    for item in keys:
        if header[item]['count'] < minsup:
            header.pop(item)

    class Node:
        def __init__(self, item=None, count=1):
            self.item = item
            self.count = count
            self.children = []
            self.parent = None

        def addChild(self, item, count=1):
            for child in self.children:
                if child.item == item:
                    child.count += count
                    return child
            new_node = Node(item=item, count=count)
            header[item]['pointers'].append(new_node)
            self.children.append(new_node)
            new_node.parent = self
            return new_node

        def __repr__(self):
            return repr("Item:"+str(self.item)+", Count:"+str(self.count))

        def __str__(self):
            return "Item:"+str(self.item)+", Count:"+str(self.count)

    def make_tree():
        root = Node()
        for t in db:
            items = list(t)
            items = list(filter(lambda x: x in header, items))
            items.sort(key=lambda x: header[x]['count'])
            curr = root
            for item in range(0, len(items)):
                curr = curr.addChild(items[item])
        return root

    root = make_tree()
    # print( root.children[0].children[0].parent,root.children[0])

    outputs = dict()

    def mine_tree(X, H):
        keys = list(H.keys())
        keys.sort(key=lambda x: H[x]['count'])
        for I in keys:
            if H[I]['count'] >= minsup:
                outputs[tuple([I]+X)] = H[I]['count']
                H_I = buildsubtable(I)
                mine_tree([I]+X, H_I)

    def buildsubtable(I):
        H_I = defaultdict(lambda: {'count': 0, 'pointers': []})

        for u in header[I]['pointers']:
            v = u.parent
            while(v.item is not None):
                v.count = 0
                v = v.parent

        for u in header[I]['pointers']:
            v = u.parent
            while(v.item is not None):
                H_I[v.item]['pointers'].append(v)
                v.count = v.count+u.count
                H_I[v.item]['count'] += u.count
                v = v.parent
        return dict(H_I)

    mine_tree([], header)
    print("Top Down")
    print(outputs)
    print(len(outputs))


def BU():
    header1 = defaultdict(lambda: {'count': 0, 'pointers': []})
    db = set()
    with open(data_file) as f:
        for line in f.readlines():
            attrs = line.strip().split('-1')
            vals = []
            for val in attrs[:-1]:
                x = val.strip()
                if x not in vals:
                    vals.append(x)
                    header1[x]['count'] += 1
            db.add(tuple(vals))

    header1 = dict(header1)
    keys = list(header1.keys())

    for item in keys:
        if header1[item]['count'] < minsup:
            header1.pop(item)

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
            return repr("Node1 Item:"+str(self.item)+", Count:"+str(self.count))

        def __str__(self):
            return "Node1 Item:"+str(self.item)+", Count:"+str(self.count)

    def make_tree1():
        root = Node1()
        for t in db:
            items = list(t)
            items = list(filter(lambda x: x in header1, items))
            items.sort(key=lambda x: header1[x]['count'], reverse=True)
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


td_start = time.time()
TD()
td_end = time.time()
print("Top Down Time:", td_end-td_start, "s")
bu_start = time.time()
BU()
bu_end = time.time()
print("Bottom Up Time:", bu_end-bu_start, "s")
