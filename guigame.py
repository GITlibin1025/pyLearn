'''
游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏。
假设游戏场景为范围（x, y）为0<=x<=10，0<=y<=10
游戏生成1只乌龟和10条鱼
它们的移动方向均随机
乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
当移动到场景边缘，自动向反方向移动
乌龟初始化体力为100（上限）
乌龟每移动一次，体力消耗1
当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
鱼暂不计算体力
当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束
'''
import random as r

#0<=范围<=10
#0<=范围<=10 
tl = 100

a = r.randint(0,11)
b = r.randint(0,11)
m = r.randint(0,11)
n = r.randint(0,11)


#-----------------------------------------
class Turtle:
	def _init_(self,a,b):
		self.a = a
		self.b = b
	def ddd(self):
		o = r.randint(0,2)
		if o == 0:#就走一步
			t = r.randint(0,4)
			if t == 0:
				y = y+1
			#上移动
			elif t == 1:
				y = y-1
			#下移动
			elif t == 2:
				y = y-1
			#左移动
			else:
				y = y+1
			#右移动
			
		else:#8种情况
			s = r.randint(0,8)
			if s==0:#1向上2
				y =y+2
			elif s==1:#2向下2
				y =y-2
			elif s==2:#3向左2
				x =x-2
			elif s==3:#4向右2
				x =x+2
			elif s==4:#5左上1
				y =y+1
				x =x-1
			elif s==5:#6左下1
				y =y-1
				x =x-1
			elif s==6:#7右上1
				y =y+1
				x =x+1
			else:#8右下1
				y =y-1
				x =x+1
			#就走两步
			
			#出圈办法n
		if y < 0:
			y = -y
		else:
			pass
		if y > 10:
			y = 20-y
		else:
			pass
	#确定位置

	#出圈办法n
		if x < 0:
			x = -x
		else:
			pass
		if x > 10:
			x = 20-x
		else:
			pass
	#初始化体力-1
		tl = tl-1
		if tl == 0:
			print ('ENG')
		else:
			pass

		global G
		G =(x,y)
#---------------------------------------
	
class Fish:
	def _init_(self,m,n):
		self.m = m
		self.n = n
	def ddd(self):
		u = r.randint(0,4)
		if u == 0:#坐标运算
			n = n+1
			#上移动
		elif u == 1:
			n = n-1
			#下移动
		elif u == 2:
			m = m-1
			#左移动
		else:
			m = m+1
			#右移动
	#检测有没有出圈
	
	#出圈办法m
		if m < 0:
			m = -m
		else:
			pass
		if m > 10:
			m = 20-m
		else:
			pass
	#出圈办法n
		if n < 0:
			n = -n
		else:
			pass
		if n > 10:
			n = 20-n
		else:
			pass
			
			
	#出圈办法n
		if m < 0:
			m = -m
		else:
			pass
		if m > 10:
			m = 20-m
		else:
			pass
		
		global F
		F =(m,n)
#-------------------------------

def game():
	if G == F:
		print('乌龟胜利')
	else:
		Turtle.ddd(self)
		Fish.ddd(self)
	

#检验坐标是否重合
	
