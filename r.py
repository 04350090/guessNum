import random
# standard library 標準函式庫
# random is a module

r = random.randint(1, 100)
count = 0
while True:
	count += 1 #count = count + 1
	num = input('請猜1到100的數字：')
	num = int(num)
	if num == r:
		print('猜對了！')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('差一點，比答案大')
	elif num < r:
		print('差一點，比答案小')
	print('這是你猜的第', count, '次')
