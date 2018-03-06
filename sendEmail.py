'''
Python Script to send update emails. 

Created By: Shiva Bhusal, BGSU 
'''
import smtplib

gmail_user = 'civabhusal@gmail.com'  
gmail_password = '$password'

sent_from = gmail_user  
to = ['sbhusal@bgsu.edu']  
subject = 'Message'  
body = 'Hey, what'

email_text = 'abcd'

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print 'Email sent!'
except:  
    print 'Something went wrong...'


