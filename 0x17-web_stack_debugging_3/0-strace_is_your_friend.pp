# fixe the wp-settings.php

exec { 'wp-set':
	command: 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	path: '/bin/'

}
