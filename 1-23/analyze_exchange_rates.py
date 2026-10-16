# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：用字串、split()、串列與字典整理資料，再以迴圈和條件統計匯率。
# 解析美元與日圓兌新臺幣的每日開盤價、收盤價資料。
# 統計各幣別最高、最低、平均收盤價與上漲天數。
raw_exchange_data = """
2026-03-15|USD/TWD|31.52|31.58
2026-03-15|JPY/TWD|0.2115|0.2110
2026-03-16|USD/TWD|31.58|31.62
2026-03-16|JPY/TWD|0.2110|0.2105
2026-03-17|USD/TWD|31.62|31.55
2026-03-17|JPY/TWD|0.2105|0.2120
2026-03-18|USD/TWD|31.55|31.50
2026-03-18|JPY/TWD|0.2120|0.2125
2026-03-19|USD/TWD|31.50|31.48
2026-03-19|JPY/TWD|0.2125|0.2130
2026-03-20|USD/TWD|31.48|31.52
2026-03-20|JPY/TWD|0.2130|0.2118
2026-03-21|USD/TWD|31.52|31.55
2026-03-21|JPY/TWD|0.2118|0.2115
2026-03-22|USD/TWD|31.55|31.60
2026-03-22|JPY/TWD|0.2115|0.2108
2026-03-23|USD/TWD|31.60|31.65
2026-03-23|JPY/TWD|0.2108|0.2100
2026-03-24|USD/TWD|31.65|31.70
2026-03-24|JPY/TWD|0.2100|0.2095
2026-03-25|USD/TWD|31.70|31.68
2026-03-25|JPY/TWD|0.2095|0.2102
2026-03-26|USD/TWD|31.68|31.62
2026-03-26|JPY/TWD|0.2102|0.2110
2026-03-27|USD/TWD|31.62|31.58
2026-03-27|JPY/TWD|0.2110|0.2118
2026-03-28|USD/TWD|31.58|31.54
2026-03-28|JPY/TWD|0.2118|0.2122
2026-03-29|USD/TWD|31.54|31.50
2026-03-29|JPY/TWD|0.2122|0.2128
2026-03-30|USD/TWD|31.50|31.45
2026-03-30|JPY/TWD|0.2128|0.2135
2026-03-31|USD/TWD|31.45|31.40
2026-03-31|JPY/TWD|0.2135|0.2140
2026-04-01|USD/TWD|31.40|31.42
2026-04-01|JPY/TWD|0.2140|0.2138
2026-04-02|USD/TWD|31.42|31.48
2026-04-02|JPY/TWD|0.2138|0.2130
2026-04-03|USD/TWD|31.48|31.52
2026-04-03|JPY/TWD|0.2130|0.2125
2026-04-04|USD/TWD|31.52|31.55
2026-04-04|JPY/TWD|0.2125|0.2120
2026-04-05|USD/TWD|31.55|31.58
2026-04-05|JPY/TWD|0.2120|0.2115
2026-04-06|USD/TWD|31.58|31.62
2026-04-06|JPY/TWD|0.2115|0.2110
2026-04-07|USD/TWD|31.62|31.65
2026-04-07|JPY/TWD|0.2110|0.2105
2026-04-08|USD/TWD|31.65|31.60
2026-04-08|JPY/TWD|0.2105|0.2112
2026-04-09|USD/TWD|31.60|31.55
2026-04-09|JPY/TWD|0.2112|0.2120
2026-04-10|USD/TWD|31.55|31.50
2026-04-10|JPY/TWD|0.2120|0.2125
2026-04-11|USD/TWD|31.50|31.46
2026-04-11|JPY/TWD|0.2125|0.2130
2026-04-12|USD/TWD|31.46|31.42
2026-04-12|JPY/TWD|0.2130|0.2138
2026-04-13|USD/TWD|31.42|31.38
2026-04-13|JPY/TWD|0.2138|0.2145
"""

# 1. 建立資料結構


# 2. 逐行剖析字串
# usd_open_prices = []
# 計算美元
usd_open_prices = []
usd_close_prices = []
for line in raw_exchange_data.strip().split("\n"):
    # 只處理 USD
    if "USD/TWD"  in line:
        # 對 '|' 進行分割
        date, pair, open_p, close_p = line.split("|")
        usd_open_prices.append(float(open_p))
        usd_close_prices.append(float(close_p))

# 計算日圓
jpy_open_prices = []
jpy_close_prices = []
for line in raw_exchange_data.strip().split("\n"):
    # 只處理 JPY
    if "JPY/TWD"  in line:
        # 對 '|' 進行分割
        date, pair, open_p, close_p = line.split("|")
        jpy_open_prices.append(float(open_p))
        jpy_close_prices.append(float(close_p))


open_prices = {
    "USD": usd_open_prices,
    "JPY": jpy_open_prices
}

close_prices = {
    "USD": usd_close_prices,
    "JPY": jpy_close_prices
}


print("Open Prices:", open_prices)
print("Close Prices:", close_prices)

# 統計指標與格式化輸出 (Formatting & Calculation)
# 這 30 天各幣別的：最高收盤價、最低收盤價、平均收盤價（四捨五入至小數第 4 位）。
# 各幣別「收盤價高於開盤價（漲）」的總天數。

max_close_prices = {currency: max(prices) for currency, prices in close_prices.items()}
min_close_prices = {currency: min(prices) for currency, prices in close_prices.items()}
avg_close_prices = {currency: round(sum(prices) / len(prices), 4) for currency, prices in close_prices.items()}

print("Max Close Prices:", max_close_prices)
print("Min Close Prices:", min_close_prices)
print("Avg Close Prices:", avg_close_prices)

# 計算各幣別「收盤價高於開盤價（漲）」的總天數
up_days = {currency: sum(1 for open_p, close_p in zip(open_prices[currency], close_prices[currency]) if close_p > open_p) for currency in open_prices}
print("Up Days:", up_days)