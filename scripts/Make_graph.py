import plotly.express as px
import pandas as pd

df = pd.read_csv("docs/WebData.csv")
fig = px.line(df, x="date", y="value")