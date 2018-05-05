#创建网页的服务器， 可设置接口
#用cmd命令行启动服务器。 文件路径找到此文件所在路径，然后执行 python simple_httpd.py 
#服务器会一直执行，直到关闭。
#开启期间其他脚本都可以修改，修改后保存即可。
from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8081

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

