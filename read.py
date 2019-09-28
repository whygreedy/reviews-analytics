
data = []
count = 0
with open('reviews.txt', 'r') as r:
	for line in r:
		data.append(line)
		count = count + 1
		if count % 1000 == 0: # %求餘數
			print(len(data))



print(len(data))
print(data[0])
print('-----分隔線-----')
print(data[1])