#!/bin/bash

cd /srv/

ls

echo "===> volume mounted. Ready to start service."
#pip3 install -r requirements.txt
while true; do
 echo "`date +'%F %T'` [INFO] Fake service running..."
 sleep 60
done
# python3 manage.py migrate
# python3 manage.py runserver 0.0.0.0:8000