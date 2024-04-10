import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import svm
from  sklearn.model_selection import train_test_split
data= pd.read_csv('bmi.csv')
print(data)
df= pd.DataFrame(data)
print(df)
plt.figure(figsize=(10, 6))
from sklearn.metrics import accuracy_score
sns.scatterplot(df, x='Weight', y='Bmi', hue='BmiClass')
plt.show()
plt.figure(figsize=(10, 6))
sns.scatterplot(df, x='Height', y='Bmi', hue='BmiClass')
plt.show()

X = df.drop('BmiClass', axis=1)
y = df['BmiClass']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

a= accuracy_score(y_test, y_pred)
print(a)