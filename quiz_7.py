from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd


#  --------------    Data Preparation  --------------
data = {
    'Bill Length(mm)': [39.1, 45.4, 40.3, 50.1, 47.2, 38.9, 49.5],
    'Flipper Length(mm)': [181, 195, 185, 205, 194, 179, 216],
    'Species': ['Adelie', 'Gentoo', 'Adelie', 'Gentoo', 'Chinstrap', 'Adelie', 'Gentoo']
}

df = pd.DataFrame(data)

# --------------  divide data => 80 train | 20 test   --------------
X = df[['Bill Length(mm)', 'Flipper Length(mm)']]
y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)  # train the model with the data

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)            #train the model with the data
y_pred_knn = knn.predict(X_test)      #predict the price of the house based on the test data
accuracy_knn = accuracy_score(y_test, y_pred_knn) #calculate the accuracy of the model
print(f'KNN Accuracy: {accuracy_knn}')

new_penguin = pd.DataFrame({'Bill Length(mm)': [42], 'Flipper Length(mm)': [192]})

predicted_knn = knn.predict(new_penguin)[0]
print(f"Predicted price of the new house (KNN): {predicted_knn}")

predicted_nb = clf.predict(new_penguin)[0]
print(f"Predicted price of the new house (Naive Bayes): {predicted_nb}")

