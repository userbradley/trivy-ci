#!/bin/sh
echo $container
trivy -q -f table i $container > trivy-out.txt
trivy -q -f json $container > scan.json
python3 ./issue.py
#@TODO: Need to make document on how to create creds, echo "username:token" | base64 then upload to codefresh