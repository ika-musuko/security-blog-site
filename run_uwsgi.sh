#!/bin/sh
uwsgi --socket 0.0.0.0:8000 --enable-threads --protocol=http -w blog_site:app
