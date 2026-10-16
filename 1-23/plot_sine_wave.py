# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：用串列保存資料、以 for 逐項計算，並透過函式分工繪製圖表。
# 計算一組弧度角的正弦值，並繪製正弦曲線。
# 範例在 -3 到 3 之間取樣並顯示圖表。
import math

import matplotlib.pyplot as plt


def func1(x):
    """Return a list of y values using y = sin(x), with x in radians."""
    y = [] # list
    for value in x:
        y.append(math.sin(value))
    return y


def draw(x, y):
    """Plot matching lists of x and y values."""
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")

    plt.figure()
    plt.plot(x, y, marker="*")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.grid(False)
    plt.show()


if __name__ == "__main__":
    start = -3
    end = 3
    num_points = 20
    step = (end - start) / (num_points - 1)
    x = []
    for index in range(num_points):
        x.append(start + index * step)

    y = func1(x)
    print(y)
    draw(x, y)