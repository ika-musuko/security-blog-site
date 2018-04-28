#!/bin/sh
sudo cp blog_site.service /etc/systemd/system/blog_site.service
sudo cp nginx_config /etc/nginx/sites-available/blog_site
