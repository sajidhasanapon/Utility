
from imaplib import IMAP4_SSL
from subprocess import call
from time import sleep

def main():
	
	sleep(20)
	login_success = False
	
	obj = IMAP4_SSL('imap.gmail.com','993')
	while login_success == False:
		try:
			obj.login('username','password')
			obj.select()
			login_success = True
		except:
			login_success = False
			
	while True:
		try:
			n = len(obj.search(None,'NOT SEEN')[1][0].split())
			if n > 0:
				call(["start", "email_notifier.bat"], shell=True)
				sleep(300)
		except:
			None


if __name__ == "__main__":
	main()
