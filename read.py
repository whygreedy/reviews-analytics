
data = []
count = 0
with open('reviews.txt', 'r') as r:
	for line in r:
		data.append(line)
		count = count + 1
		if count % 1000 == 0: # %求餘數
			print(len(data))
print('檔案讀取完了，總共用', len(data), '筆資料')


sum_len = 0
for d in data:
	sum_len += len(d)

print('每一筆留言的平均長度為', sum_len/len(data))


# 篩選出留言長度 < 100字的留言數
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])
