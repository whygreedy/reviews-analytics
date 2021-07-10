import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		bar.update(count)
print('檔案讀取完畢，共', len(data), '筆留言')

# 留言數據統計、篩選

sum_d = 0
for d in data:
	sum_d = len(d) + sum_d

print('共', sum_d, '個字')
avg = sum_d / len(data)
print('平均留言字數: ', avg)

# f > line -> data(留言清單)
# data > d(每一筆留言)
# 總字數/總留言數 = 平均每則留言字數

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('字數<100的留言數: ', len(new))


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('提及good的留言數: ', len(good))


# 文字計數

start_time = time.time()
wc = {} # word_count
for d in data:
	words = d.split()
	for w in words:
		if w in wc:
			wc[w] += 1
		else:
			wc[w] = 1
for w in wc:
	if wc[w] > 1000000:
		print(w, '出現', wc[w], '次')
end_time = time.time()
print('花了', end_time - start_time, 'seconds')
print('共', len(wc), '個字')

while True:
	print('可查詢其他字詞，結束查詢輸入q')
	w = input('想查哪個字詞: ')
	if w == 'q':
		print('結束查詢，謝謝你的使用')
		break
	if w in wc:
		print(w, '出現', wc[w], '次')
	else:
		print('很抱歉，該字詞不存在')








