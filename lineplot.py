import matplotlib.pyplot as plt

# Sample Dataset
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [5000, 7000, 6500, 8000, 9000, 8500]

plt.figure(figsize=(7,5))
plt.plot(months,sales,marker='i', label='Sales')
plt.title("monthly sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()