import yate
import cgi
import os
import time
import sys

print(yate.start_response('text/html'))
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
methon = os.environ['REQUEST_METHOD']
cur_time = time.asctime(time.localtime())
print(host + ", " + addr + ", " + cur_time + ": " + methon + ": " , end = '',file = sys.stderr )
form = cgi.FieldStorage()
for each_form_item in form.keys():
	print(each_form_item + '->' + form[each_form_item].value,end = ' ',file = sys.stderr)
print(file = sys.stderr)
print('OK')
