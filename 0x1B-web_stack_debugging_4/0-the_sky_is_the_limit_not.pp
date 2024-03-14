# Increase the number of open file for nginx service 
exec {'fix--for-nginx':
	command => '/usr/bin/env sed -i "s/15/1000/g" /etc/default/nginx'
}->

# restart nginx 
exec {'restart-nginx':
	command => '/usr/bin/env service nginx restart'
}
