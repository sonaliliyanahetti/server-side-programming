#We can use classes and methods in the HTTPServer module to create our own server.
#From the http.server we are importing two classes. We have to define the server address. To do so we use the HTTPServer class
from http.server import HTTPServer,BaseHTTPRequestHandler

#To show web pages and to handle user inputs we need to import the BaseHTTPRequestHandler class
class MyServer(BaseHTTPRequestHandler):#create a class to hold our server.In this class, we have to give outputs according to user inputs. So we have to use methods in the BaseHTTPRequestHandler class.  (that is the reason for including that class name inside brackets in our new class declaration.)
    def do_GET(self):# we can handle user requests
      if self.path == '/':
         self.path = '/index.html'
      try:
         file_to_open = open(self.path[1:]).read()
         self.send_response(200)
      except FileNotFoundError:
         file_to_open = "File not found"
         self.send_response(404)
#This line is to notify that the user has accessed the web page successfully.  
      self.end_headers()# will end the accessing process
      self.wfile.write(bytes(file_to_open,'utf-8'))

httpd =HTTPServer(('localhost',8080),MyServer)#create an HTTP variable by calling the HTTPServer class to host our servers
#define that variable as httpd.set the server address and pass this data to our MyServer class.  
httpd.serve_forever()