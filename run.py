#Import python modules

import numpy as np
import pandas as pd

#Visualisation
import matplotlib.pyplot as plt
import missingno
import seaborn as sns

#Model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve, classification_report
from sklearn.preprocessing import LabelEncoder
#Energy Usage
import energyusage

dataset = pd.read_csv("Iris.csv")
#print(dataset.head(5))
#print(dataset.info())
dataset.drop('Id', axis=1, inplace=True)
print(dataset.head(5))



#EDA

# Sepal length and width

fig = dataset[dataset.Species=='Iris-setosa'].plot(kind='scatter',x='SepalLengthCm',y='SepalWidthCm',color='orange', label='Setosa')
dataset[dataset.Species=='Iris-versicolor'].plot(kind='scatter',x='SepalLengthCm',y='SepalWidthCm',color='blue', label='versicolor',ax=fig)
dataset[dataset.Species=='Iris-virginica'].plot(kind='scatter',x='SepalLengthCm',y='SepalWidthCm',color='green', label='virginica', ax=fig)
fig.set_xlabel("Sepal Length")
fig.set_ylabel("Sepal Width")
fig.set_title("Sepal Length VS Width")
fig=plt.gcf()
fig.set_size_inches(10,6)
#plt.show()

# Petal length and width
fig = dataset[dataset.Species=='Iris-setosa'].plot.scatter(x='PetalLengthCm',y='PetalWidthCm',color='orange', label='Setosa')
dataset[dataset.Species=='Iris-versicolor'].plot.scatter(x='PetalLengthCm',y='PetalWidthCm',color='blue', label='versicolor',ax=fig)
dataset[dataset.Species=='Iris-virginica'].plot.scatter(x='PetalLengthCm',y='PetalWidthCm',color='green', label='virginica', ax=fig)
fig.set_xlabel("Petal Length")
fig.set_ylabel("Petal Width")
fig.set_title(" Petal Length VS Width")
fig=plt.gcf()
fig.set_size_inches(10,6)
#plt.show()


dataset.hist(edgecolor='black', linewidth=1.2)
fig=plt.gcf()
fig.set_size_inches(12,6)
#plt.show()


print(dataset.shape)


# split into train/test
def train_test_split(dataset, train_frac= 0.7, seed=1):
    df_matrix = dataset.values

    # shuffle the data
    np.random.seed(seed)
    np.random.shuffle(df_matrix)

    # split the data
    train_size = int(df_matrix.shape[0] * train_frac)
    # features are all except last column
    train_features  = df_matrix[:train_size, :-1]
    # the last column
    train_labels = df_matrix[:train_size, -1]

    # test data
    test_features = df_matrix[train_size:, :-1]
    test_labels = df_matrix[train_size:, -1]

    return (train_features, train_labels), (test_features, test_labels)


(train_features, train_labels), (test_features, test_labels) = train_test_split(dataset, train_frac=0.7)

lg = LogisticRegression()
lg.fit(train_features, train_labels)
lgpredict = lg.predict(test_features)
score = lg.score(test_features, test_labels)
#print(score)

pred_lg = lg.predict(test_features)
log_reg_predict_proba = lg.predict_proba(test_features)[:, 1]

print('\nLogistic Regression Accuracy: {:.2f}%'.format(accuracy_score(test_labels, lgpredict) * 100))
