'''
Python Script to check the download status and periodically send status via email. 
Created By: Shiva Bhusal, BGSU 
'''
import smtplib
import time
import sys
import subprocess

gmail_user = 'appdownload.updates@gmail.com'  
gmail_password ='$password'

sent_from = 'App Analysis Project'  
to = ['nadeez.civa@gmail.com']  

while (True):
	try:  
		lineCount=0
		with open("test_10.csv") as f: #Open the file and get the lineCount. 
			for line in f:
				lineCount=lineCount+1
		message = 'Subject: {}\n\n{}'.format('Download Updates', str(lineCount)+' APKs downloaded.')
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, to, message)
		server.close()
		print ('Email sent!')
	
	except:  
		print ('Something went wrong!')

	time.sleep(60)


