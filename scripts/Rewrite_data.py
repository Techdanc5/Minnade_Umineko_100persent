import pandas as pd

#スプシから取得したデータをDataFrameとして格納
df = pd.read_csv(
    "./scripts/GetData.csv",
    encoding="utf-8-sig"
    )

#GameCount加工用にcsvをコピー
df_calc = df.copy()

#各データの差枚数を計算し、"Samai"列を追加
df_calc["Samai"] = df_calc["GetMedals"] - df_calc["UseMedals"]

df_calc.to_csv("./scripts/UseData.csv", index=False)

print("RewriteData処理完了")