#!/bin/bash
# Make a request to the server and follow redirects
curl -sL -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
