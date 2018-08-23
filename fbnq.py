#斐波那契数列
#使用迭代

'''				#多行注释
def fab(n):
	n1 = 1
	n2 = 1
	n3 = 1 #默认初始值为1
	
	if n < 1:
		print("输入有误")
		return -1
		
	while (n-2) > 0:
		n3 = n1 + n2
		n1 = n2
		n2 = n3
		n -= 1
		
	return n3
	
x = int(input("请输入项数"))
fanhuizhi = fab(x)
if fanhuizhi != -1:
	print('该项的系数为%d' % fanhuizhi)
'''
	

	
	
	

def fab(x):
	x1 = 1
	x2 = 1
	x3 = 1	#当(x-2)<0时返回，而不是随便写的数
	
	if x < 1:
		return -1
		print('输入有误')
		
	while (x - 2) > 0:
		x3 = x1 + x2
		x1 = x2
		x2 = x3
		x -= 1
		
	return x3
	
print("------求斐波那契数列------")
print("==========================")
x = int(input("请输入项数"))
y = fab(x)
if y != -1:
	print('第%d项的系数为%d' %  (x,y))
#为格式化操作符 %d 为整数		 ^^注意当参数不为一时一定不要忘记（）
	print("--------------------------")
