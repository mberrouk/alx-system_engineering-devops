# Increase the number of open file for nginx service

# Increase open file limit
exec {'fix--for-nginx':
	command => 'sed -i "s/15/1000/g" /etc/default/nginx',
 	path    => '/usr/local/bin/:/bin/'
}->

# restart nginx 
exec {'restart-nginx':
	command => 'nginx restart',
 	path    => '/etc/init.d/'
}
