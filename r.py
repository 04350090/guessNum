import random
# standard library 標準函式庫
# random is a module
while True:
	start = input('請決定隨機數字範圍開始值：')
	end = input('請決定隨機數字範圍結束值：')
	if start.isdigit() and end.isdigit():
		start = int(start)
		end = int(end)
		if start >= end:
			print('開始值不能大於結束值！')
		elif start == end - 1:
			print('範圍太小了，請增加') 
		else:
			break
	else:
		print('請輸入數字！')		

r = random.randint(start, end)
count = 0
while True:
	count += 1 #count = count + 1
	num = input('請猜數字：')
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
