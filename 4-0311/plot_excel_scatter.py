# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：以 pandas DataFrame 讀取表格和欄位，並用 matplotlib 呼叫繪圖方法。
# 讀取 Excel 中的 x、y 欄位，計算兩欄總和並繪製散佈圖。
# 使用 pandas 讀取資料，並以 matplotlib 顯示圖表。
import pandas as pd
import matplotlib.pyplot as plt

# pip pandas
# pip install matplotlib
# pip install openpyxl

# 讀取 Excel 檔案
df = pd.read_excel('311.xlsx')

# 假設欄位名稱為 'x' 和 'y'
df['sum'] = df['x'] + df['y']

# 印出相加結果
print(df['sum'])

# 繪製散佈圖
plt.scatter(df['x'], df['y'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter plot of x and y')
plt.show()