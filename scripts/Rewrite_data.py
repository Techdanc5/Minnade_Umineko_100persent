import pandas as pd

#スプシから取得したデータをDataFrameとして格納
update_df = pd.read_csv(
    "D:\Python_Project\Minnnade_Umineko\scripts\GetData.csv",
    encoding="utf-8-sig"
    )

#書き換えを行う対象のcsvを格納
#base_df = pd.read_csv("UseData.csv")

#GameCount列
#key = "TimeStamp"
#target_col = "GameCount"

#DataFrameをindexに
#base_df = base_df.set_index(key)
#update_df = update_df.set_index(key)

#既存の列を置換
#base_df[target_col].update(update_df[target_col])

#新規列の抽出
#new_rows = update_df.loc[~update_df.index.isin(base_df.index)]
#base_df = pd.concat([base_df, new_rows], axis=0)

#base_df = base_df.reset_index()

update_df.to_csv("D:/Python_Project/Minnnade_Umineko/scripts/UseData.csv", index=False)

print("Rewritedata処理完了")