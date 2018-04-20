#Head first python 学习
#异常处理
import os
import pickle
import ex_1

man = []
other = []
new_man = []

try:
	data = open('E:/GitHub/Headfirst_python/testtry.txt')

	for each_line in data:
		try:
			(role,line_spoken) = each_line.split(':',1)
			line_spoken = line_spoken.strip()
			if role == 'man':
				man.append(line_spoken)
			elif role == 'other man ':
				other.append(line_spoken)
			
		except ValueError:
			pass
	data.close()
	
except IOError:
	print("missing file")


	
try:
	with  open('E:/GitHub/Headfirst_python/man.txt','wb') as outman: 
		#print(man,file = outman)
		pickle.dump(man,outman)
	with open('E:/GitHub/Headfirst_python/other.txt','wb') as outother: 
		#print(other,file = outother)
		pickle.dump(other,outother)
	

	print('文件写入ok') #这里写的文件在程序里面乱码了
	
except IOError as err:
	print('File error' + str(err))
except pickle.PickleError as perr:
	print('pickle error' + str(perr))	
	
try:
	with open('E:/GitHub/Headfirst_python/man.txt','rb') as man_file:
		new_man = pickle.load(man_file)
except IOError as err:
	print('File error' + str(err))
except pickle.PickleError as perr:
	print('pickle error' + str(perr))
	
ex_1.print_name(new_man)  #这里读出来的文件格式正常，是pickle处理的原因。 保存的是二进制的文件
	

	
	