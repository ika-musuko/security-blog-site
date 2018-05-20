import os
import smtplib
def send_email(message: str, address: str):

    # Credentials
    username = os.getenv("EMAIL_ADDRESS") or ''
    password = os.getenv("EMAIL_PASSWORD") or ''

    # mail is being sent :
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    print("MESSAGE - logging into gmail...")
    server.login(username,password)
    print("MESSAGE - sending mail: ADDRESS: %s CONTENTS: %s" % (address, message))
    server.sendmail(username, address, message)
    server.quit()

if __name__ == "__main__":
    send_email("hello", "7206337812@vzwpix.com")