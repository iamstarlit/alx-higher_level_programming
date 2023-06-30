#!/bin/ bash
# Sends a request to URL and displays the size of the response.
curl -s "$1" | wc -c
