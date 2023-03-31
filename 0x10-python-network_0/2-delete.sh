#!/bin/bash
# Sends a DELETE HTTP verb to Delete a resource
commandline_argument_1=$1
curl -sX DELETE "$commandline_argument_1"
