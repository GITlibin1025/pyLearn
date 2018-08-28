#通讯录工具
txl = {}

print('|---欢迎使用通讯录工具---|')
print('|----1:创建新的联系人----|')
print('|----2:删除现有联系人----|')
print('|----3:查找现有联系人----|')
print('|----4:退出通讯录工具----|')

def cx():
	temp = input('请输入相关代码')
	if temp == '1':
		xm = input('请输入姓名')
		dh = input('请输入联系电话')
		txl[xm] = dh
		cx()
	elif temp == '2':
		xm = input('请输入要删除者姓名')
		del txl[xn]
	elif temp == '3':
		xm = input('请输入要查找者姓名')
		y = txl[xm]
		print (y)
		print('是否进行修改Yes/No')
		x = input('Y/N')
		if x == 'N':
			cx()
		else:
			txl[xm] = input('输入新的电话')
	elif temp == '4':
		print('-----END-----')
	else:
		print('您输入的代码不正确')
		
cx()
	