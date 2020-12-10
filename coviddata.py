import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv(r"E:\rv\whitehatjr\python\datavisualization\coviddataplotly-\covid_data.csv")
fig = px.scatter(df, x="cases", y="country",
	           color="date",
                size_max=60)
fig.show()
