#!/bin/bash
# check if root
if [ "$(id -u)" != "0" ]; then
	echo "sudo plz"
	exit 1
fi

# start apache
apachectl stop
apachectl start

# generate rsa key
rm /private/etc/apache2/server.*
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /private/etc/apache2/server.key -out /private/etc/apache2/server.crt

# copy apache2conf
cp ./apache2/httpd.conf /etc/apache2/
cp ./apache2/extra/* /etc/apache2/extra/
cp -r ./apache2/html/* /Library/WebServer/Documents/
chmod -R 755 /Library/WebServer/Documents
apachectl restart
