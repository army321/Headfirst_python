import yate
import cgi

import sqlite3 #这个函数现在用sqlite调用，不在写到原来的腌制数据中

print(yate.start_response('text/plain'))

db_name = 'coachdate.sqlite'

form = cgi.FieldStorage()
the_id = form_data['Athlete'].value
the_time = form_data['Time'].value

connection = sqlite3.connect(db_name)
cursor = connection.cursor()
cursor.execute("INSERT INTO timing_data (athlete_id,value) VALUES(?,?)",(the_id,the_time))

connection.commit()
connection.close()


print('OK')
