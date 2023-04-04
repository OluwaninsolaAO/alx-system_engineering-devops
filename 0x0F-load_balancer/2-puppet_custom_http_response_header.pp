# Add a custom HTTP header with Puppet

exec { 'install-stdlib':
  command => 'sudo puppet module install puppetlabs-stdlib',
}

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
  line   => "add_header X-Served-By ${hostname}",
  after  => 'location / {',
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
