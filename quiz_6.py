from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pandas as pd

#  --------------    Data Preparation  --------------
data = {
    'Has Fur': [1, 0, 0, 0, 1, 0, 0, 0],     #  1 => yes, 0 => no
    'Can Fly': [0, 1, 0, 0, 1, 1, 0, 0],
    'Lays Eggs': [0, 1, 0, 1, 0, 1, 0, 1],
    'Class': ['Mammal', 'Bird', 'Mammal', 'Bird', 'Mammal', 'Bird', 'Mammal', 'Bird']
}

df = pd.DataFrame(data)

# --------------  divide data => 80 train | 20 test   --------------
X = df[['Has Fur', 'Can Fly', 'Lays Eggs']]
y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# ----------  Decision Tree Classifier ,Naive Bayes  --------------
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)  # train the model with the data

dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

# --------------  test the model and calc the accuracy  --------------
dt_preds = dt_model.predict(X_test)
nb_preds = nb_model.predict(X_test)

dt_accuracy = accuracy_score(y_test, dt_preds)
nb_accuracy = accuracy_score(y_test, nb_preds)

print(f"Decision Tree Accuracy: {dt_accuracy * 100:.2f}%")
print(f"Naive Bayes Accuracy: {nb_accuracy * 100:.2f}%")

# --------------  Predicting the class of a new animal  --------------
new_animal = pd.DataFrame({'Has Fur': [1], 'Can Fly': [0], 'Lays Eggs': [0]})
dt_result = dt_model.predict(new_animal)[0]
nb_result = nb_model.predict(new_animal)[0]
print(f"Predicted class of the new animal (Decision Tree): {dt_result}")
print(f"Predicted class of the new animal (Naive Bayes): {nb_result}")
