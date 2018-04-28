CS 166 Security Blog Web Application
====================================

Blog website made in Flask without any other Flask extensions (aka, from scratch).
python3.6
server: nginx+uwsgi
!!! **INSTALL LINUX** !!!
(i haven't tested this on windows so who knows how the dependencies will work)

Installation Instructions: run install_dependencies.sh first and then create a virtual environment and install the requirements

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
TBD


Cloud Deployment
---------------
TBD
