import os

import polars as pl

directory_path = os.getcwd()
csv_file = "RomanHoliday.csv"

# ディレクトリ内のすべてのファイルを取得
# files = os.listdir(directory_path)

# CSVファイルのみをフィルタリング
# csv_files = [file for file in files if file.endswith('.csv')]

# # 各CSVファイルを読み込み、データフレームに結合
# df_list = [pl.read_csv(os.path.join(directory_path, csv_file)) for csv_file in csv_files]
# combined_df = pl.concat(df_list)

df = pl.read_csv(os.path.join(directory_path, csv_file))
requiered_columns = ["comment-id", "comment-body"]
df = df.select(requiered_columns)

df.write_csv("../pipeline/inputs/RomanHoliday.csv")
