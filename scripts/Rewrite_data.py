import pandas as pd

#スプシから取得したデータをDataFrameとして格納
df = pd.read_csv(
    "D:\Python_Project\Minnnade_Umineko\scripts\GetData.csv",
    encoding="utf-8-sig"
    )

#GameCount加工用にcsvをコピー
df_calc = df.copy()

#各データの差枚数を計算し、"Samai"列を追加
df_calc["Samai"] = df_calc["UseMedals"] - df_calc["GetMedals"]

df_calc.to_csv("D:/Python_Project/Minnnade_Umineko/scripts/UseData.csv", index=False)

print("Rewritedata処理完了")