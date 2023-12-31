# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pjUn3s6r77I8EIQInFmjNCZm-OFT9854

Klasifikasi naive bayes dengan dataset mall customer

Kel 12
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""#import dataset"""

dataset = pd.read_csv("Mall_Customers.csv")
x = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:,-1].values

print(x)



print(y)

"""#Membagi Skala dataset"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.25, random_state=0)

"""#Merubah menjadi Skala atau Koma biar mudah di olah"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

print(x_train)

"""#buat classifier"""

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train,y_train)

"""#buat predik"""

y_pred = classifier.predict(x_test)

print(y_pred)

"""#buat matrik"""

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
sns.heatmap(cm, annot=True)
plt.xlabel("Prediction Label")
plt.ylabel("True Label")
plt.title("Confusion matrix")
plt.show()

"""#melihat acuracy"""

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)