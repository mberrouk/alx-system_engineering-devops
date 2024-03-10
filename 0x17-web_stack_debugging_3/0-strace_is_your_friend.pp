# fixe the wp-settings.php

exec { 'wp-set':
  command: '/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php'
}
