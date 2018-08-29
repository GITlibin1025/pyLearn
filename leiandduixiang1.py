'''
按照以下要求定义一个游乐园门票的类，并尝试计算2个成人+1个小孩平日票价。
平日票价100元
周末票价为平日的120%
儿童半票
'''
class mp:
	def adult_normal(self):
		a = int(100)
		return a
	def child_normal(self):
		b = int(50)
		return b
	def wa(self):
		c = int(120)
		return c
	def wc(self):
		d = int(60)
		return d

x = mp()

m = 2*x.adult_normal() + x.child_normal()
#TypeError: adult_normal() missing 1 required positional argument: 'self'
n = 2*x.wa() + x.wc()

print(m)
print(n)
 