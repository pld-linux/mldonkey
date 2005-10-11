#!/bin/sh

. /etc/sysconfig/mldonkey

set -e

if [ ! -d ~/.mldonkey ]; then
	 echo "Creating $HOME/.mldonkey"
	 mkdir $HOME/.mldonkey
   fi

cd ~/.mldonkey && exec /usr/bin/mlnetd
