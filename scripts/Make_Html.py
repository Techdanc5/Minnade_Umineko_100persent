import pandas as pd
import os
import plotly.express as px
from pathlib import Path

#総計データとして載せる為のデータを格納
df = pd.read_csv("./docs/WebData.csv")

table_html = df.to_html(
    index=False,
    border=1,
    classes="data-table"
)

df2 = pd.read_csv("./docs/GetData.csv")

fig = px.line(
    df2,
    x=df2.columns[0],
    y=df2.columns[1]
)

#graph_htmlにfigureを格納
graph_html = fig.to_html(
    full_html=False,
    include_plotlyjs=False
)

# HTML 全体を組み立て
html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>みんなでうみねこ</title>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>

<h1>みんなでうみねこ</h1>

<h2>総計データ</h2>

{table_html}

<h2>グラフ</h2>

{graph_html}

</body>
</html>
"""

Path("docs/index.html").write_text(html, encoding="utf-8")
