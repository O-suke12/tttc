import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

filename = "./RomanHoliday.csv"  # 保存するCSVファイル名
base_url = "https://eiga.com/movie/50969/review/"  # ローマの休日

url_list = [base_url]
headers = {"User-Agent": "Mozilla/5.0"}

# 次のページのURL
# /all/2 から/all/10 までを追記
for i in range(2, 11):
    url_list.append(base_url + "all/" + str(i))


# 空のリストを用意
user_ids = []  # ユーザーID
ratings = []  # 評価値
titles = []  # レビューのタイトル
reviews = []  # レビュー

# 各URLについてレビューなどを取得
for url in url_list:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    # 全てのレビュー要素を取得する
    review_elements = soup.find_all("div", class_="user-review")

    # 各レビューの情報を取得する
    for review_element in review_elements:
        # ユーザーID
        user_id = review_element["data-review-user"]

        # 評価の数値を取得する
        rating_element = review_element.find("span", class_="rating-star")
        rating = rating_element.text if rating_element else None

        # レビュータイトルを取得する
        title_element = review_element.find("h2", class_="review-title")
        title = (
            title_element.text.replace(rating, "").strip() if title_element else None
        )

        # レビュー本文を取得する
        review_text_element = review_element.find("p", class_="short")
        hidden_review_text_element = review_element.find(
            "p", class_="hidden"
        )  # ネタバレを含むレビューを入れる場合
        if review_text_element:
            review = review_text_element.text.strip()
        elif hidden_review_text_element:
            review = hidden_review_text_element.text.strip()
        else:
            review = None

        # 取得した情報をリストに追加
        user_ids.append(user_id)
        ratings.append(rating)
        titles.append(title)
        reviews.append(review)

    print(f"{url}まで終了")
    time.sleep(2)


# ---------------------------------------------------------------------
# csvファイルとして保存
# リストをPandasのDataFrameに変換
df = pd.DataFrame(
    {
        "user_id": user_ids,
        "rating": ratings,
        "title": titles,
        "review": reviews,
    }
)

df.to_csv(filename, index=False)
