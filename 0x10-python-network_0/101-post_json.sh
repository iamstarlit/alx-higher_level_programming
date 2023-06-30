#!/bin/bash
# Send a POST request with the file contents as the request body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
