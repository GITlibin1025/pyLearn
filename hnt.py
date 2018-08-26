#汉诺塔游戏求解
#总是借助一个柱子
'''
x,y,z要例如4层
x借助z将3层移动到y
y借助z将2层移动到x
x借助z将1层移动到y
#最底下盘子到z
'''
def hanoi(n,x,y,z):
	if n == 1:
		print(x,'-->',z)
	else:
		hanoi(n-1,x,z,y)#把x上的(n-1)层移动到y
		print(x,'-->',z)#把n最后一层拿到z
		hanoi(n-1,y,x,z)#将y上的(n-1)层移动到z

print("--汉诺塔游戏攻略--")
n = int(input('请输入层数'))
print(hanoi(n,'X','Y','Z'))

'''总结
参数的来回转换
'''
