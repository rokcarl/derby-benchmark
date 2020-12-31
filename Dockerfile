FROM python:3.9
RUN apt update && apt install -y openjdk-11-jdk
RUN pip install pydrda==0.4.2 numpy==1.19.4 docopt==0.6.2
ADD . /app
WORKDIR /app
CMD ["/app/run.py"]
