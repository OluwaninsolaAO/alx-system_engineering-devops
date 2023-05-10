# 0. Strace is your friend

exec { 'fix_typo_1':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}

exec { 'fix_typo_2':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/bin',
}
