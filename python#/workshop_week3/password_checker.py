import csv
import pandas as pd
from pywebio.input import *

#Your application should read the employees.csv (on Blackboard) and sort it into alphabetical order
df = pd.read_csv("employees.csv", header=None)

#df.columns = ["Last Name", "First Name"]

sorted_df = df.sort_values(by=df.columns[0])

#The app should use a drop-down menu to select members of staff
staff_list = (sorted_df[0] + " " + sorted_df[1]).tolist()
dropdown = select(label="Members of staff", options=staff_list)
print(dropdown)

#Clicking on a member of staff should add one to the count of whether they have updated their password or not
count = {}
for name in staff_list:
    i=0
    if dropdown == name:
        i+=1
        count[name] = i

print(count)

