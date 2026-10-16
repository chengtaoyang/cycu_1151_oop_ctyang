# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：用 len() 取得字串長度，以索引和 range() 逐字檢查並累積位置。
# 找出字串中大寫英文字母 I 的所有位置。
# 範例會列出兩段文字中 I 的索引。
def find_i_positions(text):
	number_list = []
	for index in range(len(text)):
		if text[index] == 'I':
			number_list.append(index)
	return number_list


string1 = "I'm a lumberjack, and I'm okay."
string2 = "I sleep all night and I work all day."

# detect all 'I' characters in the strings
i_count1 = string1.count('I')
i_count2 = string2.count('I')

positions1 = find_i_positions(string1)
positions2 = find_i_positions(string2)
print("string1:", positions1)
print("string2:", positions2)
