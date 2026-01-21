import pandas as pd
import os

df = pd.read_csv("docs/WebData.csv")

table_html = df.to_html(
    index=False,
    border=1,
    classes="data-table"
)

# HTML 全体を組み立て
html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>CSV データ公開</title>
</head>
<body>
<h1>CSV データ一覧</h1>
{table_html}
</body>
</html>
"""

# HTML 書き込み
with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(html)
