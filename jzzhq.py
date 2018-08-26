#使用递归编写一个十进制转换为二进制的函数（要求采用“取2取余”的方式，结果与调用bin()一样返回字符串形式）。
import sys
sys.setrecursionlimit(10000000)#递归深度
x = int(input('输入你想转变为二进制的数字'))
y = 0
JH = []
def bin_sz(x):
	temp_s = x//2#数学基本运算符号出现问题
	temp_y =x%2
	x = temp_s
	y = str(temp_y)
	JH.append(y)
	if x == 0:
		JH.reverse()#就将list倒着打印
		a =''.join(JH)#JH中的元素必须是字符型
		print (a)
	else:
		bin_sz(x)

bin_sz(x)
		