#!/bin/bash
# Sends GET request to URL and displays response body
curl -sX GET -H "X-School-User-Id: 98" "$@" \
