#! /usr/local/bin/python3
#点击查看成绩的时候调用这个函数 
import cgitb
cgitb.enable()

import athletemodel
import cgi
import yate
import glob

data_files = glob.glob("data/*.txt")  #成绩的源文件路径，
athletes = athletemodel.put_to_store(data_files)


print(yate.start_response())
print(yate.include_header("运动员的成绩"))
print(yate.start_form("generate_timing_data.py"))  #选择想要查询的运动员名字后，执行这个脚本
print(yate.para("选择你想要查询的运动员: " ))

for each_athlete in athletes:
	print(yate.radio_button("which_athlete",athletes[each_athlete].name)) 
print(yate.end_form("查询"))

print(yate.include_footer({"返回主页":"/index.html"}))