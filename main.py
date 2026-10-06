import pandas as pd

df = pd.read_csv("variant_data.csv", index_col="id", header=0)
n = int(input("Введите номер недели: "))

name = list(input("Введите первые 4 буквы вашей фамилии: ").upper())
ans = df.loc[n, name].values

for i in range(4):
    print(f"{i + 1} - {ans[i]}")