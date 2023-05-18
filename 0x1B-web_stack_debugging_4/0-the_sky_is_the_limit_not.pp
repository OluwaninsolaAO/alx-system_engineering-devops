# 0. Sky is the limit, let's bring that limit higher

exec { 'increase-ulimit':
   command => 'sed -i "s/15/4096/" /etc/default/nginx',
}

exec { 'restart-nginx':
   command => 'service nginx restart',
}
