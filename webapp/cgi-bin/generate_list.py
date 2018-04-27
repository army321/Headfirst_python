#! /usr/local/bin/python3
import cgitb
cgitb.enable()

import ex_7
import cgi
import yate
import glob

data_files = glob.glob("F:/github/Headfirst_python/data/*.txt")
athletes = ex_7.put_to_store(data_files)


print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("Athlete: " ))

for each_athlete in athletes:
	print(yate.radio_button("ssss",athletes[each_athlete].name))
print(yate.end_form("select"))

print(yate.include_footer({"Home":"/index.html"}))