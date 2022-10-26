FROM python:3.8.8-slim-buster
WORKDIR /tmp/build
COPY . .
RUN apt-get update -y
RUN pip3 install -r requirements.txt -t .
FROM lambci/lambda:python3.8
COPY --from=0 /tmp/build /var/task