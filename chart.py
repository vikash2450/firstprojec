import matplotlib.pyplot as plt


categories = ["Category a","category b","category c"]
values = [10,20,15]

plt.figure(figsize=(8,5))
plt.bar(categories,values, color="skyblue")

plt.title("bar chart")

plt.xlabel("fruits")
plt.ylabel("values")

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
