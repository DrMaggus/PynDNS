##########CONFIG##########


#Password (for authorization and login)

password = "wer"

#Application name => http://<AppName>.appspot.com

AppName = "pyndns"



class ENV():
	password = password
	appname = AppName


import base64
import hmac
import hashlib

def auth_code(data):
	return base64.encodestring(
		hmac.new(ENV.password, 
				unicode( data ).encode("utf-8"),
				hashlib.sha256).digest()
		).strip()
