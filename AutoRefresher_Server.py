import SocketServer
import BaseHTTPServer
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer
import threading


browsers = []
editors = []


class AutoRefresherWebSocketServerHandler(WebSocket):
	def handleConnected(self):
		browsers.append(self)
		print "Connected browser:", self.address, self.request.headers.get('User-Agent')

	def handleMessage(self):
		#print(self.data)
		pass

	def handleClose(self):
		browsers.remove(self)


#class AutoRefresherEditorServerHandler(SocketServer.BaseRequestHandler):
#	def setup(self):
#		print "Connected editor: ", self
#
#	def handle(self):
#		recv = self.request.recv(1024)
#		print(recv)
#		for b in browsers:
#			b.sendMessage(recv)
class AutoRefresherEditorServerHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		if(self.path == "/refresh"):
			for b in browsers:
				b.sendMessage("refresh")
			retmsg = "Refreshed "+str(len(browsers))+" pages!"
		else:
			retmsg = "Bad request!"

		self.send_response(200)
		self.send_header("Content-type", "text/plain")
		self.end_headers()
		self.wfile.write(retmsg)


if __name__ == '__main__':
	#HOST, PORT = "localhost", 9999

	#server = SocketServer.TCPServer((HOST, PORT), AutoRefresherEditorServerHandler)
	##server.serve_forever()
	#th1 = threading.Thread(target = server.serve_forever)
	#th1.daemon = True
	#th1.start()
	
	#server2 = SimpleWebSocketServer("localhost", 9998, AutoRefresherWebSocketServerHandler)
	#server2.serveforever()

	#WebSocket server for the browser connection
	server1 = SimpleWebSocketServer("localhost", 9998, AutoRefresherWebSocketServerHandler)
	th1 = threading.Thread(target = server1.serveforever)
	th1.daemon = True
	th1.start()

	#Simple HTTP server for the editor
	server2 = BaseHTTPServer.HTTPServer(("localhost", 9999), AutoRefresherEditorServerHandler)
	server2.serve_forever()