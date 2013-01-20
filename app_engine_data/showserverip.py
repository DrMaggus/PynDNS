import hashlib
import wsgiref.handlers
from models import IP_DB
from config import ENV
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db



class ShowServerIp(webapp.RequestHandler):
	def get(self):
		self.response.out.write( template.render('showserverip.html', {"remote_ip": self.request.remote_addr} ))
	def post(self): 
		if ( ENV.password_hash == hashlib.sha512(self.request.get('password')).hexdigest() ):
			ip = IP_DB.get_by_key_name(ENV.ip_key_name) 
			self.response.out.write("<b>"+ip.ip+"</b><br>Last Update: "+str(ip.time))
		else:
			self.response.out.write("<h1>Wrong Password</h1>")

def main():
	wsgiref.handlers.CGIHandler().run( 
			webapp.WSGIApplication([(ENV.url_show_ip, ShowServerIp)], debug=ENV.debug)
	)


if __name__ == "__main__":
	main()
