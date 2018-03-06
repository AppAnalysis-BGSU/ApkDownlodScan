'''
Python Script to check the download status and periodically send status via email. 
Created By: Shiva Bhusal, BGSU 
'''
import smtplib
import time

gmail_user = 'appdownload.updates@gmail.com'  
gmail_password ='$Password!'

sent_from = gmail_user  
to = ['nadeez.civa@gmail.com']  
subject = 'Message'  
body = 'Hey, what'

email_text = 'abcd'

while (True):
	try:  
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, to, email_text)
		server.close()
		print 'Email sent!'
	
	except:  
		print 'Something went wrong...'

	time.sleep(60)


