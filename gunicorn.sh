#!/usr/bin/env sh

gunicorn superlists.wsgi:application
