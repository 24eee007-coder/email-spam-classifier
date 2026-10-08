import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/emails.csv")

sns.countplot(x="Prediction", data=df)
plt.xticks([0, 1], ["Ham", "Spam"])
plt.title("Spam vs Ham Count")
plt.show()