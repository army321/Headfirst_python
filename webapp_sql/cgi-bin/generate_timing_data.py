#! /usr/local/bin/python3

import cgi
import athletemodel
import yate





#处理选中选手的数据
form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value
athlete = athletemodel.get_athlete_from_id(athlete_id)

#用yata里面的内容返回成网页可以理解的内容
print(yate.start_response())
print(yate.include_header("运动员的成绩"))
print(yate.header("运动员：" + athlete['Name'] + ",   出生日期：" + athlete['DOB'].dob + " ."))
print(yate.para("最好成绩: " ))

print(yate.u_list(athlete['top3']))

print(yate.para("the entire set of timing data is: " + str(athlete['data']) + "(duplicates removed)."))

print(yate.include_footer({"返回主页":"/index.html","查看其他运动员成绩": "generate_list.py"}))
