#Head first python 学习
#处理数据
import os

#jake.txt,james.txt,long.txt,susan.txt
'''
with open('E:/GitHub/Headfirst_python/kelly/jake.txt') as jakef:
	data = jakef.readline()
	jake = data.strip().split(',')
with open('E:/GitHub/Headfirst_python/kelly/james.txt') as jamesf:
	data = jamesf.readline()
	james = data.strip().split(',')
with open('E:/GitHub/Headfirst_python/kelly/long.txt') as longf:
	data = longf.readline()
	long = data.strip().split(',')
with open('E:/GitHub/Headfirst_python/kelly/susan.txt') as susanf:
	data = susanf.readline()
	susan = data.strip().split(',')
	#优化成一个函数
'''

def get_coach_data(filename):
	try:
		with open('E:/GitHub/Headfirst_python/kelly/'+filename) as f:
			data = f.readline()
		return(data.strip().split(','))
	except IOError as ioerr:
		print('file error' + ioerr)
		return(None)


def sanitize(time_string):   #替换文本中的连接符，统一用.  传入的是一个数据，先拆分在组合
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins,sece)=time_string.split(splitter)
	return (mins + '.' +sece)	

jake = get_coach_data('jake.txt')
james = get_coach_data('james.txt')
long = get_coach_data('long.txt')
susan = get_coach_data('susan.txt')
	
clean_jake = []
clean_james = []

for each in jake:
	if each not in clean_jake:
		clean_jake.append(sanitize(each)) #把处理过的数据在添加到数组里面。
for each in james:
	clean_james.append(sanitize(each))
	
	
print (sorted(clean_jake[0:3]))
print (sorted(clean_james))

print(sorted(set([sanitize(t) for t in long]))[0:3]) #这里是另外一种写法。

