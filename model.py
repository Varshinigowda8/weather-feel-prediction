from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from data import temps, labels

# --- KNN Model ---
knn_model = KNeighborsClassifier(n_neighbors=1)
knn_model.fit(temps, labels)

def predict_knn(temp):
    return knn_model.predict([[temp]])[0]

# --- Decision Tree Model ---
tree_model = DecisionTreeClassifier()
tree_model.fit(temps, labels)

def predict_tree(temp):
    return tree_model.predict([[temp]])[0]

# --- Logistic Regression Model ---
log_model = LogisticRegression(max_iter=200)
log_model.fit(temps, labels)

def predict_logistic(temp):
    return log_model.predict([[temp]])[0]
