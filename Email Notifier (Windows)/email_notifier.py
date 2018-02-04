
from imaplib import IMAP4_SSL
from subprocess import call
from time import sleep
def main():
	sleep(20)

	obj = IMAP4_SSL('imap.gmail.com','993')
	obj.login('username','password')
	obj.select()
	
	while True:
		n = len(obj.search(None,'NOT SEEN')[1][0].split())
		if n > 0:
			call(["start", "email_notifier.bat"], shell=True)
		sleep(300)
		


if __name__ == "__main__":
	main()
