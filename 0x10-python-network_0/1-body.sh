#!/bin/bash
# This script returns the contents of body response if a Status Code of 200 is reported
commandline_argument_1=$1
status_code=$(curl -sLI "$commandline_argument_1" | grep 200|  cut -d " " -f 2)
page_body=$(curl -sL "$commandline_argument_1")

if test "$status_code" = "200"
then
	echo -n "$page_body";
fi

