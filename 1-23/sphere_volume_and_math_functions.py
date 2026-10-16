# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：透過 import 使用模組函式與常數，並以算術運算組合數學公式。
# 示範使用 math 模組計算球體體積、三角函數與自然常數。
# 同時展示 exp() 與次方運算的結果。
import math
#part 1
r = 5
volume = math.pow(5,3) * math.pi *4 /3
print ('part1 volume=', volume)

#part 2
x = 42 
v =  math.sin(x) **2 + math.cos(x) **2

print ('part2 =' ,v)

#part 3
print ('math.e=', math.e)
print ('math.e ** 2=', math.e ** 2)
print ('math.e', math.pow(math.e, 2))

math.exp(2)
print ('math.exp(2)=', math.exp(2))
