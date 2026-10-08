import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/emails.csv")

X = df.drop(columns=["Email No.", "Prediction"])
y = df["Prediction"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

models = {
    "Naive Bayes": MultinomialNB(),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "SVM": LinearSVC(max_iter=5000),
}

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(f"\n{name}")
    print("Accuracy :", round(accuracy_score(y_test, pred), 4))
    print("Precision:", round(precision_score(y_test, pred), 4))
    print("Recall   :", round(recall_score(y_test, pred), 4))
    print("F1 Score :", round(f1_score(y_test, pred), 4))
    import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

best = LogisticRegression(max_iter=1000)
best.fit(X_train, y_train)
cm = confusion_matrix(y_test, best.predict(X_test))

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Ham", "Spam"], yticklabels=["Ham", "Spam"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Logistic Regression")
plt.show()
import joblib
import os

os.makedirs("model", exist_ok=True)
joblib.dump(best, "model/model.pkl")
joblib.dump(list(X.columns), "model/columns.pkl")
print("Model saved!")