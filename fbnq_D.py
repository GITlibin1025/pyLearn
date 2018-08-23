#知道A1 = 1 ，A2 = 1
'''
def xianshu(num):
	if 0< num < 3:
		return 1
	elif num > 2:
		return  xianshu(num - 1)+xiangshu(num - 2)

print('--------斐波那契数列--------------')
a = input("请输入项数")
x = int(a)
y = xianshu(x)
print(y)
'''
#使用递归
def fab(x):
	if x < 1:
		print("输入错误 ")
		return -1
		#print("输入错误 ")		print命令要在return之前
	elif x == 1 or x == 2:
		return 1
	else :
		return fab(x-1)+fab(x-2)
		
a = input("请输入项数")
x = int(a)
y = fab(x)
print(y)