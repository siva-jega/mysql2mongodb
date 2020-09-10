FROM centos:latest

# Install Python 3 and pip
RUN yum update -y && \
    yum install -y python3 \ 
    python3-pip \
    python3-devel \
    mysql-devel \
    gcc 

RUN pip3 install flask pymongo mysqlclient

WORKDIR /app

#Bring shell for interactive action
#ENTRYPOINT [ "python3" , "main.py"]

CMD [sh]
