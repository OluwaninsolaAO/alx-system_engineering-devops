#!/usr/bin/env bash
# This script creates an executable bash script
# with its starting shebang indentifier.

if test -n "$1"; then
	echo "#!/usr/bin/env bash" >> $1
	chmod u+x $1
	vi $1
else
	echo "Usage: create ``FILENAME``"
fi
