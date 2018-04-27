import pickle
from athletelist import AthleteList

#为数据建模，把txt数据存到内存中 put_to_store
#然后可以到内存中获得数据。get_from_store

#path = 'F:/github/Headfirst_python/kelly/'   #要加入路径

def get_coach_data(filename):  #打开文件的函数
	try:
		with open(filename) as f:
			data = f.readline()
			templ = data.strip().split(',')
			
		return(AthleteList(templ.pop(0),templ.pop(0),templ))
	except IOError as ioerr:
		print('file error' + ioerr)
		return(None)
		
def put_to_store(file_list):
	all_athletes = {}
	for each_file in file_list:
		ath = get_coach_data(each_file)
		all_athletes[ath.name] = ath
	try:
		with open('athletes.pickle','wb') as athf:
			pickle.dump(all_athletes,athf)
	except IOError as ioerr:
		print('File error(put_to_store)' + str(ioerr))
	return(all_athletes)
	
def get_from_store():
	all_athletes = {}
	try:
		with open('athletes.pickle','rb') as athf:
			all_athletes = pickle.load(athf)
	except IOError as ioerr:
		print('File error(get_from_store)' + str(ioerr))
	return(all_athletes)
	
'''
#结构测试代码	
the_file = ['susan2.txt','long2.txt']
data1 = put_to_store(the_file)
print(data1)

for each_athlete in data1:
	print(data1[each_athlete].name + ' ' + data1[each_athlete].dob)
	

data_copy = get_from_store()
for each_athlete in data_copy:
		print(data_copy[each_athlete].name + ' ' + data_copy[each_athlete].dob)
'''		