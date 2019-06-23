FROM ubuntu:latest
MAINTAINER Nathan Coulson "nathancoulson@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ADD . /app_3
WORKDIR /app_3
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app3.py"]