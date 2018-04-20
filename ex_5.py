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

#path = 'E:/GitHub/Headfirst_python/kelly/'  
path = 'F:/github/Headfirst_python/kelly/'  
#206
#创建类
class Athlete:
	def __init__(self,a_name,a_dob = None, a_times = []):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times
		
	def top3(self):
		return(sorted(set([sanitize(t) for t in self.times]))[0:3])


def get_coach_data(filename):  #打开文件的函数
	try:
		with open(path+filename) as f:
			data = f.readline()
			templ = data.strip().split(',')
			
		return(Athlete(templ.pop(0),templ.pop(0),templ))
		#{'Name':templ.pop(0),
		#		'DOB':templ.pop(0),
		#		'Times':str(sorted(set([sanitize(t) for t in templ]))[0:3])})
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

susan2 = get_coach_data('susan2.txt')
#print(susan2)
#(susan_name,susan_dob) = susan2.pop(0),susan2.pop(0) #去掉头2个元素
#print(susan_name + "'s fastest time are : " + str(sorted(set([sanitize(t) for t in susan2]))[0:3]))

#print(susan2['Name'] + "'s fastest time are : " + susan2['Times'])

print(susan2.name + "'s fastest time are : " + str(susan2.top3()))

'''
#这部分移到函数里面去
#创建字典保存信息
susan_data = {}
susan_data['Name'] = susan2.pop(0)
susan_data['DOB'] = susan2.pop(0)
susan_data['Times'] = susan2
print(susan_data['Name'] + "'s fastest time are : " + str(sorted(set([sanitize(t) for t in susan2]))[0:3]))
'''
	
'''	
#简单数据的处理方式，没有名字和出生日期。
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
'''
