#从标准库中string模块导入 Template类
from string import Template

path = 'F:/github/Headfirst_python/'   #要加入路径
include_header_file = 'templates/header.html'
include_footer_file = 'templates/footer.html'


def start_response(resp = "text/html"):
	return('Conten-type: ' + resp + '\n\n')
	
def include_header(the_title):
	with open(include_header_file) as headf:
		head_text = headf.read()
	header = Template(head_text)
	return(header.substitute(title = the_title))
	
def include_footer(the_links):
	with open(include_footer_file) as footf:
		foot_text = footf.read()
	link_string = ''
	for key in the_links:
		link_string  += '<a href = "' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
	footer = Template(foot_text)
	return(footer.substitute(links = link_string))

def start_form(the_url, form_type = "POST"):
	return('<form action="' + the_url + '"method="' + form_type + '">')

def end_form(submit_msg = "Submit"):
	return('<p></p><imput type = submit value="' + submit_msg  + '">')

def radio_button(rb_name, rb_value):
	return('<imput type = "radio" name="' + rb_name  + '"value = "' +rb_value + '">' + rb_value + '<br />')
	
	
def u_list(items):
	u_string = '<ul>'
	for item in items:
		u_string += '<li>' + item + '</li>'
	u_string += '</ul>'
	return(u_string)
	
def header(header_text, header_level = 2):
	return('<h' + str(header_level) + '>' + header_text + '</h' + str(header_level) + '>')
	
def para(para_text):
	return('<p>' + para_text + '</p>')
	
	
'''	
print(include_header("welcom to my"))

print(include_footer({'Home':'/index.html','select':'/cgi-bin/select/py'}))
'''