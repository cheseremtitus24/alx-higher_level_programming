#!/bin/bash
# Sends a DELETE HTTP verb to Delete a resource
commandline_argument_1=$1
curl -X DELETE -s "$commandline_argument_1" -H "Connection: close"
