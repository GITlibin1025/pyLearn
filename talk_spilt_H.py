#函数方法
def write(boy,girl,count):
	file_name_boy = 'boy_'+str(count)+'.txt'
		file_name_girl = 'girl_'+str(count)+'.txt'
		
		boy_file = open(file_name_boy,'w')
		girl_file = open(file_name_girl,'w')
		
		boy_file.writelines(boy)
		girl_file.writelines(girl)
		
		boy_file.close()
		girl_file.close()



def file_split():
	f = open('123.txt')

	boy = []
	girl = []
	count = 1

	for each_line in f:
		if each_line[:3] != '===':
			(role,line_spoken) = each_line.split(':',1)#进行分割字符串的操作
			if role == '小甲鱼':
				boy.append(line_spoken)
			if role == '小客服':
				girl.append(line_spoken)
		else:
			write(boy,girl,count)
		
			boy = []
			girl = []
			count += 1
		
	write(boy,girl,count)
		

	f.close()
		
		
file_spilt()