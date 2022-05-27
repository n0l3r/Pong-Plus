FROM centos:latest

RUN cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

RUN yum update -y
RUN yum install -y glibc-locale-source

# Installing X11 and the X Window System
RUN  yum install -y dbus-x11 PackageKit-gtk3-module libcanberra-gtk2 

WORKDIR /pong-plus
COPY . /pong-plus/

RUN yum install python3 python3-pip -y
RUN pip3 install -r requirements.txt

# Starting Pong application
CMD  ["python3", "main.py"]