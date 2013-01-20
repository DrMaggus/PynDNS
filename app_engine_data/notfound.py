import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template


class NotFound(webapp.RequestHandler):
	def get(self):
		self.response.out.write( template.render('notfound.html', {} ))
	def post(self):
		self.get()

def main():
	wsgiref.handlers.CGIHandler().run( 
			webapp.WSGIApplication([(r'/.*', NotFound)], debug=False)
	)


if __name__ == "__main__":
	main()
