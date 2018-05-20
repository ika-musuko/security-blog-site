# CS 166 Security Blog Web Application

Blog website made in Flask for CS 166 discussing and demonstrating various topics in Information Security  
I avoided using any SQL ORMs, rolled out my form verification, and handled sessions myself (as opposed to Flask-Login) as specified so I didn't have any unfair advantages against those using JSP and Apache.  

## Software Stack
It's not XAMPP, it's not LAMP, it's....LNUMP???  
- **L**inux
- **N**ginx -> like Apache
- **U**wsgi -> like Tomcat
- **M**ariaDB
- **P**ython (Flask) -> like Java/JSP

## Grade Points
### Blog Site
- [X] registration screen
- [X] login screen
- [X] blog list screen
- normal user
    - [ ] add blog item
    - [ ] delete own blog item
- admin user
    - [ ] delete any blog item
- [X] logout

### Security Features
- [X] **authentication**: hashed and salted passwords
- [X] **authorization**: normal and admin roles implemented
- [X] **availability**: registration must have a captcha
- [X] **session management**: use sessions to correctly remember the user
- [X] injection attack prevention (except for attack demo)
- [X] forms use POST method
- [X] forms have CSRF prevention (except for attack demo)


### Required Content
- first blog item by me talking about how i made this
    - [ ] firewall rules
    - [ ] info about security features
- [ ] footer with privacy statement page
- [ ] at least 3 other CS 166 relevant blog items

### Feature Demonstrations
- [ ] SQL injection attack demo and how to prevent it
- [ ] XSS injection attack and possible defenses
- [ ] website defacing
- [ ] demonstrate how cookies work
- [ ] demonstrate how session management works
 
### Bonus Features
- [X] Bootstrap styling
- [ ] Edit own post
- [X] Two-step e-mail verification for new users

### Cloud Deployment
- [ ] DigitalOcean Droplet on NGINX

## Install Instructions

Dependencies:
- Python 3.6
- MariaDB

1. Clone this repository
2. Set up MariaDB on your server
3. Run `> source reset_database.sql` in MariaDB to allocate the tables (they're in database `blog_site` if you want to poke around)
4. `$ grep -rnw . -e os.getenv` and set your environment variables accordingly, I recommend making them in a file called `setenv.sh` and running as `. ./setenv.sh` so you don't have to manually set it every time. (not included)
5. Install the requirements from `requirements.txt` (please use a python virtual environment)
6. If you set your environment variables using a script like I did, you can use `./run_server.sh` to run, otherwise you can do `python main.py`
