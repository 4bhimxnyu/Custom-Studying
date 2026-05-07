import matplotlib.pyplot as plt
students = ["Rahul", "Amit", "Sneha", "Priya", "Karan"]

marks = [85, 90, 78, 88, 95]

ages = [20, 21, 19, 20, 22]

plt.figure(figsize=(10, 5))
plt.bar(students, marks)
plt.title("Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(students, ages)
plt.title("Ages of Students")
plt.xlabel("Students")
plt.ylabel("Ages")
plt.show()

