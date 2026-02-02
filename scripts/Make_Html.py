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

#グラフ用データの格納
df2 = pd.read_csv("./docs/UseData.csv")

#plotlyの作成
fig = px.line(
    df2,
    x="GameCount",
    y="Samai",
    markers=True,
    title="差枚グラフ"
)

#x軸に負の数を表示させない
fig.update_xaxes(
    range=[
        0,
        df2["GameCount"].max()*1.0
    ],
    title="ゲーム数"
)

#y軸の表示倍率をフレキシブルに

y_max = df2["Samai"].max()
y_min = df2["Samai"].min()

fig.update_yaxes(
    range=[
        min(0,y_min * 1.2),
        y_max * 1.2
    ],
    title="差枚"
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

<h2>差枚推移グラフ</h2>

{graph_html}

</body>
</html>
"""

Path("docs/index.html").write_text(html, encoding="utf-8")
