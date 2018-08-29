'''
类和对象
按照以下提示尝试定义一个矩形类并生成类实例对象。
属性：长和宽版权属于
方法：设置长和宽 -> setRect(self)，获得长和宽 -> getRect(self)，获得面积 -> getArea(self)
提示：方法中对属性的引用形式需加上 self，如 self.width'xdu
'''
class Rectangle():
	def setRect():
		print('请输入矩形的长和宽')
		global a
		global b
		a = input('长：')
		b = input('宽：')
	def getRect():
		print("这个矩形的长是 %s" % a )
		print("这个矩形的宽是 %s" % b )
	def getArea():
		Area = int(a)*int(b)
		print("这个矩形的面积是 %d " % Area)
Rectangle.setRect()
Rectangle.getRect()
Rectangle.getArea()