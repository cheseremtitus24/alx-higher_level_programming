#!/bin/bash
# This command captures the content length of data sent from a web server
curl -sI "$1" | grep Content-Length:| cut -d ':'  -f 2
