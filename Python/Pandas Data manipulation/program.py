import pandas as pd

# Load CSV File
data = pd.read_csv("file.csv")

# Display dataset
print("\nDataset:\n")
print(data)

# Mean
mean_marks = data["Marks"].mean()

# Median
median_marks = data["Marks"].median()

# Mode
mode_marks = data["Marks"].mode()[0]

# Display Results
print("\nStatistics")
print("----------------")

print("Mean:", mean_marks)
print("Median:", median_marks)
print("Mode:", mode_marks)