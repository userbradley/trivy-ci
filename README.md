# Trivy Container scanning CI

## Project breakdown
This is a CI designed application used for scanning containers using [Trivy](https://github.com/aquasecurity/trivy) and then subsequently creates a github issue for the container if there are sec issues

This application is packaged as a docker file, but can easily be run stand alone

## How this works
1. Container is set using an envirometn variable
2. `init.sh` starts the container scan using trivy, and creates 2 output files. One in json and one a text file.
3. Python picks up these files and checks if there were any CVE's:
   1. Yes: Creates a github issue and prints the Issue URL to the output
   2. Prints no sec issues on the container
4. Exits

## Setup authentication
As this is an application that interfaces with the github API, you will need to create a Toke. 
These can be made [Here](https://github.com/settings/tokens), create one with <!--@TODO: Verify --> (Coming soon, just select repo)
Base 64 encode it like below:
```bash
echo "ghusername:token" | base64
```
Where `ghusername` is your github username, and `token` is... The token we just created
## Env variables that are required
In order to use this application, there are a few enviroment variables that need to be set for the docker container.

| Env variable   | Required | Description                                                                                                         | Example                                                                                  |
|----------------|----------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| `gh_token`     | `yes`    | The base64 encoded token from above                                                                                 | `Ym9mYTpIYXZlWW91U2VlbkJvZmFEZWV6TnV0c0hBQUFBQUFBQUFHT1RFRUVFRUVFRU0K`                   |
| `container`    | `yes`    | The URL to the container, or if on docker hub, `username/container:tag`                                             | `nginx:latest` or `quay.io/codefresh/alpine:3.11`                                        |
| `gh_username`  | `yes`    | The start of the URL, or your github username if creating it under your account                                     | if the repo is `https://github.com/userbradley/issuetesting` this would be `userbradley` |
| `gh_repo_name` | `yes`    | The repo name                                                                                                       | Continuing on from the above, we would use `issuetesting`                                |
| `debug`        | `no`     | This just spits out the Response to teh API call, if you get a `404` there is most likely an issue with the API key | `true`                                                                                   |                                                                                          | 

## Using this
This application is designed to run both locally (On the command line), using docker as well as in a CI enviroment (That supports docker)
### Running Locally
To run this locally, you will need:
* python3
* pip3
* trivy `0.19.2`
1. Once these are installed, install the required python packages
```python
pip3 install -r reqs.txt
```
2. Once this is completed, set the enviroment variables as required, personally I use `direnv` for this
3. Change the permissions on `init.sh` with `chmod +x init.sh` 
4. Run `init.sh` with `./init.sh`


### Running locally using docker
Rename the file `envfile.example` to `envfile` and modify the values currently in there, then run the below
```bash
docker pull userbradley/trivy-ci:0.19.2-0.1.1
docker run --env-file ./envfile  userbradley/trivy-ci:0.19.2-0.1.1
```
### Example env file
I have provided one in this repository for you, locate it [here](/envfile.example)
### Running on Codefresh
<!-- @TODO: Test on codefresh -->

---
## Expalining the versioning format
The formatting follows the regex string of `[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,3}[-][0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,3}`
I am laying out the versioning like:

| Section | Example  | What it means                          |
|---------|----------|----------------------------------------|
| `1`     | `0.19.2` | Trivy version                          | 
| `2`     | `0.1.0`  | My release version of the docker image |

Once you've made your changes, open a PR. I will deal with the rest. 




# Other stuff:

## Known issues:
1. [No env variable validation](https://github.com/userbradley/trivy-ci/issues/4) « Suggested by an employee of [PAH](https://www.petsathome.com)
2. `404` from github » See [Github Docs](https://docs.github.com/en/rest/overview/other-authentication-methods#basic-authentication)

## Reporting an issue:
Please create an issue on github, I will get to it when I can!

## Contributing:
Please fork this to your account, increment the latest version, make your changes then open a PR.
