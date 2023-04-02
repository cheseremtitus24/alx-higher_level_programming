#!/bin/bash
# Returns All Available supported HTTP Verbs
curl -X OPTIONS -s -I "$1" | grep "Allow: " | cut -d " " -f 2,3,4 | tr -d '\r'
