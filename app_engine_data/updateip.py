import base64
import hmac
import hashlib
import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext import db
from models import IP_DB
from config import ENV



class UpdateIp(webapp.RequestHandler):
	def get(self):
		self.error(405)
	def post(self):
		auth_code = base64.encodestring(
				hmac.new(ENV.password, 
						unicode( self.request.body ).encode("utf-8"),
						hashlib.sha256).digest()
				).strip()
		if ( auth_code == self.request.headers["Authorization"] ):
			db = IP_DB(key_name=ENV.ip_key_name, ip=self.request.body)
			db.put()
			self.response.out.write("0")
		else:
			self.error(401)
		

def main():
	wsgiref.handlers.CGIHandler().run(
			webapp.WSGIApplication([(ENV.url_update_ip, UpdateIp)], debug=ENV.debug)
	)


if __name__ == "__main__":
	main()
