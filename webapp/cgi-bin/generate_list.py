#! /usr/local/bin/python3
import cgitb
cgitb.enable()

import ex_7
import cgi
import yate
import glob

data_files = glob.glob("F:/github/Headfirst_python/webapp/data/*.txt")
athletes = ex_7.put_to_store(data_files)


print(yate.start_response())
print(yate.include_header("运动员的成绩"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("选择你想要查询的运动员: " ))

for each_athlete in athletes:
	print(yate.radio_button("which_athlete",athletes[each_athlete].name))
print(yate.end_form("查询"))

print(yate.include_footer({"返回主页":"/index.html"}))