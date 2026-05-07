import pandas as pd

from sklearn.linear_model import LogisticRegression, LinearRegression

from sklearn.metrics import accuracy_score, mean_squared_error

from sklearn.impute import SimpleImputer

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler


# Dataset
data = {

    "Age": [25, 40, 35, 50, None, 45, 60, 30],

    "PreviousTreatments": [1, 2, 1, 3, 2, None, 4, 1],

    "LifestyleScore": [7, 5, 8, 4, 6, 5, 3, None],

    "MedicalCost": [2000, 5000, 3000, 7000, 4500, 6000, 9000, 2500],

    "Readmission": [0, 1, 0, 1, 0, 1, 1, 0]
}


# Create DataFrame
df = pd.DataFrame(data)

print("Dataset:\n")

print(df)


# =====================================================
# HANDLE MISSING VALUES
# =====================================================

imputer = SimpleImputer(strategy="mean")

df[["Age", "PreviousTreatments", "LifestyleScore"]] = imputer.fit_transform(

    df[["Age", "PreviousTreatments", "LifestyleScore"]]
)


# =====================================================
# FEATURE SCALING
# =====================================================

X = df[["Age", "PreviousTreatments", "LifestyleScore"]]

scaler = StandardScaler()

X = scaler.fit_transform(X)


# =====================================================
# LINEAR REGRESSION
# =====================================================

# Target Variable
y1 = df["MedicalCost"]


# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(

    X, y1, test_size=0.2, random_state=42
)


# Create Model
lr = LinearRegression()


# Train Model
lr.fit(X_train, y_train)


# Predict
pred1 = lr.predict(X_test)


# Calculate Error
mse = mean_squared_error(y_test, pred1)


print("\nLinear Regression")

print("----------------------")

print("Predicted Medical Cost:")

print(pred1)

print("Mean Squared Error:", mse)


# =====================================================
# LOGISTIC REGRESSION
# =====================================================

# Target Variable
y2 = df["Readmission"]


# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(

    X, y2, test_size=0.2, random_state=42
)


# Create Model
log_model = LogisticRegression()


# Train Model
log_model.fit(X_train, y_train)


# Predict
pred2 = log_model.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, pred2)


print("\nLogistic Regression")

print("----------------------")

print("Predicted Readmission:")

print(pred2)

print("Accuracy:", accuracy)