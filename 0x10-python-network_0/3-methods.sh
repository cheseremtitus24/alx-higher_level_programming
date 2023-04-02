#!/bin/bash
# Returns All Available supported HTTP Verbs
curl -X OPTIONS -sI "$1" | grep "Allow: " | cut -d " " -f 2,3,4 | tr '\r' ' '
