# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：用 input() 讀取文字並轉成整數，以 % 取餘數，再用 if/else 分支。
# 輸入一個整數，判斷並顯示它是奇數或偶數。
x = int(input("Enter a number: "))

if x%2 == 0:
    print ('x is even')
else:
    print ('x is odd')