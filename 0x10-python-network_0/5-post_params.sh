#!/bin/bash
# Sends a GET HTTP verb with a Header value set
curl -sX POST -d email="test@gmail.com" -d subject="I will always be here for PLD" "$1"
