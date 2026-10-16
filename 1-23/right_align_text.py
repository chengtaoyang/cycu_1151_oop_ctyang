# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：函式參數接收字串，len() 計算長度，字串乘法產生指定數量空格。
# 將文字靠右對齊至固定寬度後印出。
# 範例示範多個不同長度的字串。
def print_right(s):
    print(" "*(70-len(s))+s)
    


print_right("Monty")
print_right("Python's")
print_right("Flying Circus")