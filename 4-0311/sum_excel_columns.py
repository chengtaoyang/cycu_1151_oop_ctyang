# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：用 pandas 讀取 Excel 成為 DataFrame，以欄位名稱選取資料並進行相加。
# 讀取 Excel 檔案中的 x、y 欄位，計算每列的總和。
# 將各列加總結果印出。
import pandas as pd

# 讀取 Excel 檔案
df = pd.read_excel('311.xlsx')

# 假設欄位名稱為 'x' 和 'y'
df['sum'] = df['x'] + df['y']

# 印出相加結果
print(df['sum'])