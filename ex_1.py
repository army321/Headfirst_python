#Head first python 学习
#函数有默认的值，在使用的时候无需填相应的值
names = ['Jh','j2',['k1','k2'],'m1',['q1','q2']]



def print_name(the_list,indent = False,level =0):
	for x in the_list:
		if isinstance(x,list):
			print_name(x,indent,level+1)
		else:
			if indent:
				for tab_stop in range(level):
					print('\t',end = '')
			print(x)
			
#print_name(names,True,1)
