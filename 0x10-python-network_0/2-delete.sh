#!/bin/bash
# Sends a DELETE HTTP verb to Delete a resource
commandline_argument_1=$1
curl -X DELETE "$commandline_argument_1"
