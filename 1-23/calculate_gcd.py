# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：定義帶參數與回傳值的函式，並用條件判斷和遞迴重複計算。
# 使用遞迴輾轉相除法計算兩個整數的最大公因數。
# 範例會計算並印出 55 與 21 的最大公因數。
def gcd(a: int, b: int) -> int:
    """使用輾轉相除法（遞迴）計算兩個整數的最大公因數"""
    if b == 0:
        return a
    return gcd(b, a % b)

# 測試範例
x, y = 55, 21
print(f"GCD of {x} and {y} is {gcd(x, y)}")
