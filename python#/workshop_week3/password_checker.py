import csv
import pandas as pd

df = pd.read_csv("employees.csv")

df.columns = ["Last Name", "First Name"]

print(df.sort_values(by="Last Name"))