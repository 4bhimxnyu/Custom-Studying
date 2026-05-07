import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix

data = {

    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],

    "Result": ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass", "Pass", "Pass"]
}

df = pd.DataFrame(data)
print("dataset: ")
print(df)

df["Result"] = df["Result"].map({"Fail":0, "Pass":1})

x = df[["StudyHours"]]
y = df["Result"]


model = LogisticRegression()
model.fit(x, y)
predictions = model.predict(x)
print("Predictions: ", predictions)

accuracy = accuracy_score(y, predictions)
print("\n Accuracy: ", accuracy)
conf_matrix = confusion_matrix(y, predictions)
print("\n Confusion Matrix: \n", conf_matrix)
