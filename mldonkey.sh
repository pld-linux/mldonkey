#!/bin/sh
set -e

if [ ! -d ~/.mldonkey ]; then
	echo "Creating ~/.mldonkey"
	mkdir ~/.mldonkey
fi

cd ~/.mldonkey && exec /usr/sbin/mlnetd
