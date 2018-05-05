#! /usr/local/bin/python3

import cgi
import athletemodel
import yate



#从模型得到数据
athletes = athletemodel.get_from_store()

#处理选中选手的数据
form_data = cgi.FieldStorage()
athelete_name = form_data['which_athlete'].value

#用yata里面的内容返回成网页可以理解的内容
print(yate.start_response())
print(yate.include_header("运动员的成绩"))
print(yate.header("运动员：" + athelete_name + ",   出生日期：" + athletes[athelete_name].dob + " ."))
print(yate.para("最好成绩: " ))

print(yate.u_list(athletes[athelete_name].top3))


print(yate.include_footer({"返回主页":"/index.html","查看其他运动员成绩": "generate_list.py"}))
