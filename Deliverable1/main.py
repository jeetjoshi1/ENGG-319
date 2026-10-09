
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Gasoline": [22, 25, 28, 30, 27, 26, 24, 29, 23, 31, 22, 25, 28, 32, 26],
    "Diesel": [35, 38, 40, 37, 36, 39, 34, 38, 33, 37, 35, 39, 40, 36, 33]
}

efficiency = pd.DataFrame(data)


print("First five rows:")
print(efficiency.head())
print("\n" + "-" * 40 + "\n")

print("Value at row 0, column 1:")
print(efficiency.iloc[0, 1])
print("\n" + "-" * 40 + "\n")

print("Value at row 5, column 1:")
print(efficiency.iloc[5, 1])
print("\n" + "-" * 40 + "\n")

print("All rows from column 1:")
print(efficiency.iloc[:, 1])
print("\n" + "-" * 40 + "\n")

print("Rows 3 to 6:")
print(efficiency.iloc[3:7])
print("\n" + "-" * 40 + "\n")

print("Rows 0 to 2 from column 0:")
print(efficiency.iloc[0:3, 0])


'''
efficiency.plot(kind='box', title='Boxplot of efficiencies of Gasoline and Diesel vehicles')

plt.ylabel('Efficiency (MPG)')
plt.show()
'''