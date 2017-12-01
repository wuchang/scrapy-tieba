#!/usr/bin/env bash

python yqadmin/manage.py migrate && python yqadmin/manage.py runserver 0.0.0.0:1100 
