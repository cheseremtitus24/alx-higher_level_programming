#!/bin/bash
# This script returns the contents of body response if a Status Code of 200 is reported
commandline_argument_1=$1
status_code=$(curl -sL -o /dev/null -w "%{http_code}" "$commandline_argument_1");
redir_url=$(curl -s -o /dev/null -w "%{redirect_url}" "$commandline_argument_1")

page_body=$(curl -X GET -sL "$redir_url")

if test "$status_code" = 200
then
	echo -n "$page_body";
fi

