#定义一个类实现摄氏度到华氏度的转换（转换公式：华氏度 = 摄氏度*1.8+32）

class C2F:
	def __init__(self,ssd):
		self.ssd = ssd * 1.8 + 32
	def __str__(self):
		return str(self.ssd)
