import base64
import hmac
import hashlib
import subprocess
from urllib2 import urlopen, Request

####################################################

#Password (for authorization and login)
PASSWORD = "wer"

#Application name => http://<AppName>.appspot.com
APPNAME = "pyndns"

####################################################

def auth_code(data):
	return base64.encodestring(
		hmac.new(PASSWORD, 
				unicode( data ).encode("utf-8"),
				hashlib.sha256).digest()
		).strip()

def getIP():
	req = Request("http://"+APPNAME+".appspot.com/get", data="GET")
	req.add_header("Authorization", auth_code("GET"))

	return urlopen(req).read().strip()


if __name__ == "__main__":
	subprocess.call(["ssh", getIP()])
