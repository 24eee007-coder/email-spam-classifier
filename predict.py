import joblib
import re
import pandas as pd

model = joblib.load("model/model.pkl")
columns = joblib.load("model/columns.pkl")

def predict(text):
    words = re.findall(r"[a-z]+", text.lower())
    counts = {col: 0 for col in columns}
    for w in words:
        if w in counts:
            counts[w] += 1
    row = pd.DataFrame([counts])
    result = model.predict(row)[0]
    return "Spam" if result == 1 else "Ham"

