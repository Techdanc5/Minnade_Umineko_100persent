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

#列名の不可視文字・空白を除去
df2.columns = (
    df2.columns
    .str.replace("\ufeff", "", regex=False)
    .str.strip()
)

#数値に変換
df2["GameCount"] = pd.to_numeric(df2["GameCount"], errors="coerce")
df2["Samai"] = pd.to_numeric(df2["Samai"], errors="coerce")

#累積データを計算するカラムの追加
df2["GameCount_CumSum"] = df2["GameCount"].cumsum()
df2["Samai_CumSum"] = df2["Samai"].cumsum()

#plotlyの作成
fig = px.line(
    x=df2["GameCount_CumSum"],
    y=df2["SamaiCumSum"],
    markers=True,
    title="差枚グラフ"
)

#x軸に負の数を表示させない
fig.update_xaxes(
    range=[
        0,
        df2["GameCount"].max()*1.0
    ],
    fixedrange=True,
    title="ゲーム数"
)

#y軸の表示倍率をフレキシブルに
y_max = df2["Samai_CumSum"].max()
y_min = df2["Samai_CumCum"].min()

fig.update_yaxes(
    range=[
        min(0,y_min * 1.2),
        y_max * 1.2
    ],
    fixedrange=True,
    title="差枚"
)

#グラフの可視性アップ
fig.update_traces(
    line=dict(
        width=2,
        color="#000000"
    ),
    marker=dict(
        size=5,
        color="#000000"
    )      # 点を大きく
)

#graph_htmlにfigureを格納
graph_html = fig.to_html(
    full_html=False,
    include_plotlyjs="cdn"
)

# HTML 全体を組み立て
html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>みんなでうみねこ</title>
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
