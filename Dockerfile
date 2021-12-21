#MAINTAINER bradley@breadnet.co.uk
FROM aquasec/trivy:0.19.2
WORKDIR /app
COPY reqs.txt init.sh issue.py ./
RUN apk add python3 py3-pip
RUN pip3 install -r reqs.txt
ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]