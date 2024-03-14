# Increase the number of open file for nginx service 

exec {'fix--for-nginx':
	command => "/bin/sed -i 's/15/1000/g' /etc/default/nginx && /usr/bin/env service nginx restart"
}
