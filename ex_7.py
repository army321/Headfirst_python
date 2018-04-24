import pickle
from athletelist import AthleteList

#为数据建模，把txt数据存到内存中 put_to_store
#然后可以到内存中获得数据。get_from_store

def get_coach_data(filename):  #打开文件的函数
	try:
		with open(path+filename) as f:
			data = f.readline()
			templ = data.strip().split(',')
			
		return(AthleteList(templ.pop(0),templ.pop(0),templ))
		#{'Name':templ.pop(0),
		#		'DOB':templ.pop(0),
		#		'Times':str(sorted(set([sanitize(t) for t in templ]))[0:3])})
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