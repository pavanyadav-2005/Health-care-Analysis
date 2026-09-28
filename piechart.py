import matplotlib.pyplot as plt
x=["male","female"]
y=[1311.15,1715.45]
plt.pie(y, labels=x, autopct="%1.1f%%")
plt.title("sum of income")
plt.show()