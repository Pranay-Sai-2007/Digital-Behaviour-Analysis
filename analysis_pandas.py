import pandas as pd


df = pd.read_csv("digital_behaviour.csv")


df.head()

app1 = df["Instagram_Minutes"]

app1 = app1[0:7]

print(f"Total Minutes : {app1.sum()}\nAverage Minutes : {round(app1.mean())} \nMaximum Minutes: {app1.max()} \nMinimum Minutes : {app1.min()}")

app2 = df["Study_Minutes"]

app2 = app2[0:7]

print(f"Total Minutes : {app2.sum()}\nAverage Minutes : {round(app2.mean())} \nMaximum Minutes: {app2.max()} \nMinimum Minutes : {app2.min()}")