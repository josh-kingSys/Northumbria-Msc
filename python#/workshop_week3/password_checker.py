import csv
import pandas as pd
from pywebio.input import *

#Your application should read the employees.csv (on Blackboard) and sort it into alphabetical order
df = pd.read_csv("employees.csv", header=None)

#df.columns = ["Last Name", "First Name"]

sorted_df = df.sort_values(by=df.columns[0])

#The app should use a drop-down menu to select members of staff
select(label="Members of staff", options=sorted_df[1:])

