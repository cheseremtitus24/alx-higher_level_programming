#!/bin/bash
# Sends a DELETE HTTP verb to Delete a resource
curl -X DELETE -s "$1" -H "Connection: close"
