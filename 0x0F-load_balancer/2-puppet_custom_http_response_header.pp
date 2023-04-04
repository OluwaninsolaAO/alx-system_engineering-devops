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
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'location / {',
}

service { 'nginx':
  ensure  => 'restart',
  require => Package['nginx'],
}
