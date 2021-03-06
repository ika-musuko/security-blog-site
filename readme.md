# CS 166 Security Blog Web Application

website: http://security-blog.sherwyns.life/

This is a blog website made in Flask for CS 166 discussing and demonstrating various topics in Information Security  
I avoided using any SQL ORMs, rolled out my own form verification, and handled sessions myself (as opposed to using a third-party session management library such as Flask-Login) as specified so I didn't have any unfair advantages against those using JSP and Apache.  


## Software Stack
*It's not XAMPP, it's not LAMP, it's....LNUMP???*  
- **L**inux
- **N**ginx -> like Apache
- **U**wsgi -> like Tomcat
- **M**ariaDB
- **P**ython (Flask) -> like Java/JSP

I chose to use this stack because I have had prior experience with it (check out my latest project, [Suicide Chess](https://suicidechess.org)). However, I do recognize that my stack is slightly "modern" (aka, I get to cheat sometimes), but unlike most web frameworks, Flask is a micro-webframework, which means I am free to choose any architecture I want; Flask itself only provides URL routing, HTML templating (through Jinja2), and a primitive API for accessing sessions and cookies. 

 

I have MariaDB manually set up and running as a service on the machine and I'm using a library called [PyMySQL](https://github.com/PyMySQL/PyMySQL) to interact with it. This library requires you to write raw SQL queries so I can use this to demonstrate SQL injection attacks and how to write secure SQL code. I argue that my software stack is even *closer* to what's actually going on as I don't get a nice GUI like XAMPP where I can start and stop services with a click of a button (not that there's anything wrong with that). Additionally, I can monitor the database by running `$ mysql` and run custom queries for testing.

I chose Linux over Windows as I have more experience with Linux. I get control of every aspect of the system. This does result it in being easier to shoot yourself in the foot if you're not careful (for example, I accidentally deleted some MariaDB configuration files and spent about an hour trying to do a clean re-install) but I gain a better understanding of the overall architecture. I also believe that Linux's filesystem is more intuitive than Windows's. 

## Grade Points
### Blog Site
- [X] registration screen
- [X] login screen
- [X] blog list screen
- normal user
    - [X] add blog item
    - [X] delete own blog item
- admin user
    - [X] delete any blog item
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
    - [X] firewall rules
    - [X] info about security features
- [X] footer with privacy statement page
- [X] at least 3 other CS 166 relevant blog items

### Feature Demonstrations
- [X] SQL injection attack demo and how to prevent it
- [X] XSS injection attack and possible defenses
- [ ] website defacing
- [X] demonstrate how cookies work
- [X] demonstrate how session management works
 
### Bonus Features
- [X] Bootstrap styling
- [X] Edit own post
- [X] Two-step e-mail verification for new users
- [X] Markdown styling for blog posts
- [X] View all users
- [X] Home page post pagination (from scratch)

### Cloud Deployment
- [X] DigitalOcean Droplet on NGINX

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
