#!/usr/bin/env ruby

$from = ARGV[0].scan(/\[from:(.+?)\]/).join()
$to = ARGV[0].scan(/\[to:(.+?)\]/).join()
$flags = ARGV[0].scan(/\[flags:(.+?)\]/).join()

puts "#$from,#$to,#$flags"
