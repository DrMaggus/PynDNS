import base64
import hmac
import hashlib
import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext import db
from models import IP_DB
from config import ENV



class GetIp(webapp.RequestHandler):
	def post(self):
		auth_code = base64.encodestring(
				hmac.new(ENV.password, 
						unicode( self.request.body ).encode("utf-8"),
						hashlib.sha256).digest()
				).strip()
		if ( auth_code == self.request.headers["Authorization"] ):
			ip = IP_DB.get_by_key_name(ENV.ip_key_name) 
			self.response.out.write(ip.ip)
		else:
			self.error(401)
	def get(self):
		self.error(405)
		

def main():
	wsgiref.handlers.CGIHandler().run(
			webapp.WSGIApplication([(ENV.url_get_ip, GetIp)], debug=ENV.debug)
	)


if __name__ == "__main__":
	main()
