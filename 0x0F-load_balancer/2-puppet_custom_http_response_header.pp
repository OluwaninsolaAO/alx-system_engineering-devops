# Add a custom HTTP header with Puppet

include stdlib

exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'installed',
}

file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/nginx.conf',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'include \/etc\/nginx\/sites-enabled\/\*;',
}

service { 'nginx':
  ensure  => 'running',
  enable  => 'true',
  require => Package['nginx'],
}

exec { 'restart-nginx':
  command => '/etc/init.d/nginx restart',
}
