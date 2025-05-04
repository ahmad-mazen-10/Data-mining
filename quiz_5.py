import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

data = {
    'Size': [1500, 2000, 2200, 3000, 2700, 1800, 2500, 3200],
    'Bedrooms': [2, 3, 3, 4, 4, 3, 3, 5],
    'Price': ['Affordable', 'Affordable', 'Moderate', 'Expensive', 
              'Moderate', 'Affordable', 'Moderate', 'Expensive']
}

df = pd.DataFrame(data)

X = df[['Size', 'Bedrooms']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ------------- train and test KNN -------------
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)  #train the model with the data
y_pred_knn = knn.predict(X_test) #predict the price of the house based on the test data
accuracy_knn = accuracy_score(y_test, y_pred_knn) #calculate the accuracy of the model
print(f'KNN Accuracy: {accuracy_knn}')

# ------------- Naive Bayes Classifier  -------------
nb = GaussianNB()
nb.fit(X_train, y_train)

y_pred_nb = nb.predict(X_test)
accuracy_nb = accuracy_score(y_test, y_pred_nb)
print("Naive Bayes Accuracy:", accuracy_nb)

# -------------     predicting the price of a new house -------------
new_house = pd.DataFrame({'Size': [2500], 'Bedrooms': [4]})

predicted_price_knn = knn.predict(new_house)[0]
print(f"Predicted price of the new house (KNN): {predicted_price_knn}")

predicted_price_nb = nb.predict(new_house)[0]
print(f"Predicted price of the new house (Naive Bayes): {predicted_price_nb}")


