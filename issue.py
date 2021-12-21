import requests
import json
import os
token = os.getenv('gh_token')
container = os.getenv('container')
user = os.getenv('gh_username')
repo = os.getenv('gh_repo_name')
debug = os.getenv('debug')
url = f"https://api.github.com/repos/{user}/{repo}/issues"
user_url = f"https://github.com/{user}/{repo}/issues"


with open('scan.json', 'r') as j:
  json_data = json.load(j)
  search = (json_data[0])
  vuln_exist = "Vulnerabilities" in search

if vuln_exist == True:
  fi = open("trivy-out.txt", "rt", )
  files = fi.read()
  payload = json.dumps({
    "title": "test",
    "body": ("```" + (str(files)) + "```")
  })
  fi.close()
  headers = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': ("basic " + token),
    'contentType': 'text/x-markdown'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  if debug == "true":
    print(response.text)
  else:
    data = response.json()
    query = json.dumps(data)
    a = json.loads(query)
    issue_num = (a["number"])
    print(user_url + "/" + str(issue_num))
else:
  print("Container " + os.getenv('container') + " has no security issues" )