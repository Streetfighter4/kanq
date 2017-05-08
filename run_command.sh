#!/bin/sh

DJANGO_SETTINGS_MODULE=kanq.settings
export $DJANGO_SETTINGS_MODULE
./manage.py ${*}
