#!/usr/bin/env bash
# This script creates an executable ruby script
# with its starting shebang indentifier.

if test -n "$1"; then
	echo "#!/usr/bin/env ruby" > $1
	echo "puts ARGV[0].scan(/127.0.0.[0-9]/).join" >> $1
	chmod u+x $1
	vi $1
else
	echo "Usage: '$0' ``FILENAME``"
fi
