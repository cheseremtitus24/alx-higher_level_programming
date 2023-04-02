#!/bin/bash
# Sends a GET HTTP verb with a Header value set
curl -X GET -sH "X-School-User-Id: 98" "$1" ;
