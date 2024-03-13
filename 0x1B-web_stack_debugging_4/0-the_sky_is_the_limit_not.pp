# Increase the number of open file for nginx service 

exec {'fix--for-nginx':
	command => "/bin/sed -i 's/15/4096/g' /etc/default/nginx && /usr/bin/service nginx restart"
}
