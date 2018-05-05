#! /usr/local/bin/python3

import cgi
import ex_7
import yate



#从模型得到数据
athletes = ex_7.get_from_store()

#处理选中选手的数据
form_data = cgi.FieldStorage()
athelete_name = form_data['which_athlete'].value

#用yata里面的内容返回成网页可以理解的内容
print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("generate" + athelete_name + ",dob" + athletes[athelete_name].dob + " ."))
print(yate.para("Athlete: " ))

print(yate.u_list(athletes[athelete_name].top3))


print(yate.include_footer({"Home":"/index.html","select another antlent": "generate_list.py"}))
