#!/bin/bash
# Sends a DELETE HTTP verb to Delete a resource
curl -X OPTIONS -sI "$1" | grep "Allow: " | cut -d " " -f 2,3,4
