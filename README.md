### PYNDNS

A simple program to provide a fix dns without using dyndns or something.

Requirements:

- Root server (with python 2.7.3)
- Google App Engine Account


How it works:
The server runs the 'updateserverip.py' script with a cronjob.
The script posts the ip of the server to your google application,
which stores the ip value. To update as well as to get the ip you 
have to be authorized. There is a webpage available where you can
see the actual ip address of your server.
You can as well (after typing in your password) redirect to your
servers website.



TODO:
- Create a google application @ https://appengine.google.com/
- Customize the 
	- /app_engine_data/app.yaml 
	- /app_engine_data/config.py
	- /server_data/config.py
  files
- Deploy the data contained in /app_engine_data/ to your google appe engine
- Install Python >= 2.7.3 on your server
- Copy the /server_data/ folder to your server
- Configure your cronjob table (to run updateserverip.py every X minutes)
- Done.


Now you can run sshconnect.py from a client to connect to your server or
you can visit the website to know the ip of it.


NOTE: After the first update hasn't been made you'll get an error.
(Because there is no existing data, yet)


Recommended:
Create a bash alias for your sshconnect.py to connect to your server via ssh.

