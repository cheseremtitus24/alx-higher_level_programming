#!/bin/bash
# Sends a DELETE HTTP verb to Delete a resource
curl -sIX OPTIONS $1 | grep Allow | cut -d ':' -f 2
