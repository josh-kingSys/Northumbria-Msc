from pywebio.output import *
import pandas as pd
import plotly.express as px

population_year = []
population_number = []

file = open("newcastle_population.csv", 'r')

for line in file:
    population_number.append(int(line.split(',')[1].rstrip()))
    population_year.append(int(line.split(",")[0]))

file.close()

df = pd.DataFrame({
    'year' : population_year,
    "population" : population_number
})

fig = px.line(
    df, x="year", y="population", title="Newcastle Population 1950-2024", height=525, markers=True
)

html = fig.to_html(include_plotlyjs='require', full_html=False)

put_html(html)