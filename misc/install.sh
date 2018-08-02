#!/bin/bash

yum install git
yum install ntpdate
yum update nss curl

pip3 install --upgrade pip

pip3 install gevent
pip3 install gunicorn
pip3 install requests
pip3 install django
pip3 install mysqlclient
pip3 install uuid
pip3 install pandas
pip3 install fcoin

pip3 install django-crontab
