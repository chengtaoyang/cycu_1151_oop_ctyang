# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：函式接收參數並回傳多個值，呼叫 math 函式後以繪圖函式呈現結果。
# 將極座標轉換成笛卡兒座標，並在座標平面標示結果。
# 範例也示範呼叫函式與重複印出文字。
import math
import matplotlib.pyplot as plt


def polar_to_cartesian(r, thita):
    return r * math.cos(thita), r * math.sin(thita)


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def print_twice(string):
    print(string)
    print(string)


print_lyrics()

print_twice('Spam')

x,y =polar_to_cartesian(10, math.pi/6)
print(x, y)

# 繪製極座標轉換後的點在笛卡爾座標系中的位置
plt.scatter(x, y, color="red")  #畫圖00
plt.annotate(f"({x:.2f}, {y:.2f})", (x, y), xytext=(8, 8), textcoords="offset points")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.show()
