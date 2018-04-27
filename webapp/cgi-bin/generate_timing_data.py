#! /usr/local/bin/python3

import cgi
import ex_7
import yate




athletes = ex_7.get_from_store()

form_data = cgi.FieldStorage()
athelete_name = form_data['which_athelete'].value

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("generate" + athelete_name + ",dob" + athletes[athelete_name].dob + " ."))
print(yate.para("Athlete: " ))

print(yate.u_list(athletes[athelete_name].top3()))


print(yate.include_footer({"Home":"/index.html","select another antlent": "generate_list.py"}))
