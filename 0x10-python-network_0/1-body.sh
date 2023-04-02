#!/bin/bash
# This script returns the contents of body response if a Status Code of 200 is reported
curl -X GET -sL "$1"
