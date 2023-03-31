#!/bin/bash
# Sends a DELETE HTTP verb to Delete a resource
if [ -z "$1" ]; then
  echo "Please provide a URL as an argument."
  exit 1
fi
commandline_argument_1=$1
curl -X DELETE -s "$commandline_argument_1" -H "Connection: close"
