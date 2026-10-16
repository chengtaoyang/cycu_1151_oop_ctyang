# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：將檔案路徑存入字串變數，呼叫 pandas 函式讀取並輸出表格。
# 使用 pandas 讀取 Excel 檔案並顯示表格內容。
# 執行前請將檔案路徑改成實際的 Excel 檔案位置。
import pandas as pd
#

# Display a message
# Read the Excel file
file_path = '/path/to/your/excel/file.xlsx'
df = pd.read_excel(file_path)

# Display the data
print(df)