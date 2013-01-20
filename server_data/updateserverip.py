from config import ENV, auth_code
from urllib2 import urlopen, Request




def parseIP(html):
	return html[html.find("<!--REMOTE_IP ")+len("<!--REMOTE_IP "):html.find(" /REMOTE_IP-->")]


if __name__ == "__main__":
	req = Request("http://"+ENV.appname+".appspot.com/ip")
	data = parseIP( urlopen(req).read() ) 
	req = Request("http://"+ENV.appname+".appspot.com/update", data = data)
	req.add_header("Authorization", auth_code(data))

	res = urlopen(req).read()
	
	if (res == "0"):
		#print "Updated server ip successfully."
		pass
	else:
		print res
