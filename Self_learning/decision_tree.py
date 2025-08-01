# -*- coding: utf-8 -*-
"""Decision_tree

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/135sKYLBcB-7rA5z4rdVeVqQ5H2Qry8cU
"""

from sklearn.datasets import load_iris

data = load_iris()

X, y = data.data, data.target

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit(X, y)



from sklearn import tree
print(tree.export_text(clf))

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(50,30))
_ = tree.plot_tree(clf, feature_names=data.feature_names, class_names=data.target_names, filled=True)

tree.export_graphviz(clf, out_file="tree.dot", feature_names=data.feature_names, class_names=data.target_names, filled=True)

