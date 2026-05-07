import pandas as pd

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error


# Sample Dataset
data = {

    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],

    "Scores": [35, 40, 50, 55, 65, 70, 80, 85]
}

df = pd.DataFrame(data)
print("dataset: ")
print(df)

X = df[["StudyHours"]]
Y = df["Scores"]

model = LinearRegression()
model.fit(X, Y)
predictions = model.predict(X)
print("Predictions: ", predictions)


mse = mean_squared_error(Y, predictions)
print("\n Mean Squared Error: ", mse)