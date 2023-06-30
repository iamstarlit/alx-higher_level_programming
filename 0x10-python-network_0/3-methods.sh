#!/bin/bash
# Displays all HTTP OPTIONS allowed by the server..
curl -sI "$@" | grep -i "Allow" | cut -d " " -f 2- \
