##########CONFIG##########

# URL Handlers
# Don't forget to makes changes in the app.yaml file, as well

# Show server IP
url_ssip = r'/ip'

# Update server IP (HTTP_POST)

url_upip = r'/update'
# Get Sever IP (HTTP_GET)

url_getip = r'/get'

# Redirect page
url_redirect = r'/redirect'

#URL Header end


# Password (for authorization and login)
password = "wer"

# key_name for ip database entry
ip_key_name = "%0%"

# Debug modus
debug = "True"




import hashlib

class ENV():
	url_show_ip = url_ssip
	url_update_ip = url_upip
	url_get_ip = url_getip
	url_redirect = url_redirect
	password_hash = hashlib.sha512(password).hexdigest()
	password = password
	ip_key_name = ip_key_name
	debug = debug

