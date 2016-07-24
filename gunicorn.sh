#!/usr/bin/env sh

HOST=cdated.com
APP=superlists-staging

gunicorn --bind unix:/tmp/$APP.$HOST.socket superlists.wsgi:application
