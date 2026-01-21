import pandas as pd
import os

df = pd.read_csv(
    "D:/Python_Project/Minnnade_Umineko/scripts/UseData.csv",             
    encoding="utf-8-sig"
    )

#各データの差枚数を計算し、"Samai"列を追加
df["Samai"] = df["UseMedals"] - df["GetMedals"]

#GameCount加工用にcsvをコピー
df_calc = df.copy()

#トータルゲーム数の計算
TotalGameCount = int(df_calc["GameCount"].sum())

#トータル差枚数の計算
TotalMedalDiffernce = int(df_calc["Samai"].sum())

#docsフォルダの作成

os.makedirs("docs", exist_ok=True)

#samaiの計算を行ったデータを、csvに再度書き込む
df_calc.to_csv("docs/WebData.csv", index=False)

print("ReadCsv処理完了")