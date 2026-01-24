import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
import json
import os

# 認証スコープ
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# 認証情報読み込み・ローカル実行時
#credentials = Credentials.from_service_account_file(
#    "json/umineko-484407-5b4367aa7a8e.json",
#    scopes=scope
#)

#認証情報読み込み・GithubActions向け
if "GOOGLE_CREDENTIALS" not in os.environ:
    raise RuntimeError("GOOGLE_CREDENTIALS is not set")

credentials = json.loads(os.environ["GOOGLE_CREDENTIALS"])

# クライアント生成
gc = gspread.authorize(credentials)

# URLからスプシを読み込む
spreadsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/12I7OxaESbzjgXbSZj26gorqlCVuhnl8bCt_ZgpE4pdA/edit?resourcekey=&gid=785494444#gid=785494444')

#データを取得するシートの指定
worksheet = spreadsheet.worksheet("GetData")
data = worksheet.get_all_records()
df = pd.DataFrame(data)

#タイムスタンプ行の削除
df.drop(columns='タイムスタンプ', inplace=True)

#ヘッダ名の変更
df.rename(columns={
    'ゲーム数' : 'GameCount',
    '投入枚数' : 'UseMedals',
    '回収枚数' : 'GetMedals'
    },
    inplace=True
    )

#ローカルのcsvへ書き込み
output_path = r"./scripts/GetData.csv"
df.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)

print("GetData処理完了")