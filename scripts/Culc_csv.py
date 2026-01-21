import pandas as pd
import os

df = pd.read_csv(
    "D:/Python_Project/Minnnade_Umineko/scripts/UseData.csv",             
    encoding="utf-8-sig"
    )


#GameCount加工用にcsvをコピー
df_calc = df.copy()

#トータルゲーム数の計算
TotalGameCount = int(df_calc["GameCount"].sum())

#総投入メダル数の計算
TotalUseMedalsCount = int(df_calc["UseMedals"].sum())

#総払い出しメダル数の計算
TotalGetMedalsCount = int(df_calc["GetMedals"].sum())

#トータル差枚数の計算
TotalMedalDiffernce = int(df_calc["Samai"].sum())

#DataFrameに格納
df_final = pd.DataFrame(
    [{
        "総ゲーム数" : TotalGameCount,
        "総投入メダル数" : TotalUseMedalsCount,
        "総払い出しメダル数" : TotalGetMedalsCount,
        "総差枚数" : TotalMedalDiffernce
    }]
)

#samaiの計算を行ったデータを、csvに再度書き込む
df_final.to_csv("docs/WebData.csv", index=False)

print("ReadCsv処理完了")