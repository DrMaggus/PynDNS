from google.appengine.ext import db

class IP_DB(db.Model):
	time = db.DateTimeProperty(auto_now_add=True)
	ip = db.StringProperty(required=True)
