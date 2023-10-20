#모든 ramdom state는 42로 고정하시오.

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = load_wine()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size= 0.2, random_state = 42)
X_hold, X_test, y_hold, y_test = train_test_split(X_test, y_test, test_size= 0.5, random_state = 11)

# Load necessary libraries and data
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

data = load_wine()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size= 0.2, random_state = 42)
X_hold, X_test, y_hold, y_test = train_test_split(X_test, y_test, test_size= 0.5, random_state = 11)

# Create two LogisticRegression models
model1 = LogisticRegression(random_state=42)
model2 = LogisticRegression(penalty='l2', random_state=42)

# Train both models on the training dataset
model1.fit(X_train, y_train)
model2.fit(X_train, y_train)

# Evaluate accuracy on training and holdout validation sets
train_acc1 = accuracy_score(y_train, model1.predict(X_train))
train_acc2 = accuracy_score(y_train, model2.predict(X_train))
holdout_acc1 = accuracy_score(y_hold, model1.predict(X_hold))
holdout_acc2 = accuracy_score(y_hold, model2.predict(X_hold))

# Print the results
print("Model 1 (no regularization) - Training accuracy: {:.2f}, Holdout validation accuracy: {:.2f}".format(train_acc1, holdout_acc1))
print("Model 2 (L2 regularization) - Training accuracy: {:.2f}, Holdout validation accuracy: {:.2f}".format(train_acc2, holdout_acc2))

from sklearn.svm import SVC

# Create an SVM model with the given parameters
model = SVC(kernel='rbf', gamma=5, C=1000, random_state=42)

# Train the model on the training dataset
model.fit(X_train, y_train)

# Evaluate accuracy on training and holdout validation sets
train_acc = accuracy_score(y_train, model.predict(X_train))
holdout_acc = accuracy_score(y_hold, model.predict(X_hold))

# Print the results
print("SVM classifier - Training accuracy: {:.2f}, Holdout validation accuracy: {:.2f}".format(train_acc, holdout_acc))

gamma = 5
C = 1000