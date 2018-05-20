CS 166 Security Blog Web Application
====================================

Blog website made in Flask for CS 166 discussing and demonstrating various topics in Information Security  
I avoided using any SQL ORMs and rolled out my form verification as specified so I didn't have any unfair advantages against those using JSP and Apache.  

###software stack
- backend: python3.6/flask + mariadb
- middle tier: nginx + uwsgi running on linux
- frontend: html/css/js/bootstrap  
!!! **INSTALL LINUX** !!!<br/>
(i haven't tested this on windows so who knows how the dependencies will work)<br/>

Blog Site
---------
- [ ] registration screen
- [ ] login screen
- [ ] blog list screen
- normal user
    - [ ] add blog item
    - [ ] delete own blog item
- admin user
    - [ ] delete any blog item
- [ ] logout

Security Features
-----------------
- [ ] **authentication**: hashed and salted passwords
- [ ] **authorization**: normal and admin roles implemented
- [ ] **availability**: registration must have a captcha
- [ ] **session management**: use sessions to correctly remember the user
- [ ] injection attack prevention (except for attack demo)
- [ ] forms use POST method
- [ ] forms have CSRF prevention (except for attack demo)


Required Content
----------------
- first blog item by me talking about how i made this
    - [ ] firewall rules
    - [ ] info about security features
- [ ] footer with privacy statement page
- [ ] at least 3 other CS 166 relevant blog items

Feature Demonstrations
----------------------
- [ ] SQL injection attack demo and how to prevent it
- [ ] XSS injection attack and possible defenses
- [ ] website defacing
- [ ] demonstrate how cookies work
- [ ] demonstrate how session management works
 
Bonus Features
--------------
- [X] Bootstrap styling
- [ ] Edit own post
- [ ] Article search

Cloud Deployment
---------------
- [X] DigitalOcean Droplet on NGINX with ufw firewall
