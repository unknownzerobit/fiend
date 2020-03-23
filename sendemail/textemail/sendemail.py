#sendemail-fiend version coding by unknownzerobit

from subprocess import call
from time import sleep
from termcolor import colored

print('''
		        
		███████╗██╗███████╗███╗   ██╗██████╗ 
		██╔════╝██║██╔════╝████╗  ██║██╔══██╗
		█████╗  ██║█████╗  ██╔██╗ ██║██║  ██║
		██╔══╝  ██║██╔══╝  ██║╚██╗██║██║  ██║
		██║     ██║███████╗██║ ╚████║██████╔╝
		╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ 
                                                ''')
startcolor=colored("\n"+"########## Please don't use it as evil purposes :( ########## " ,"blue")
print("{}".format(startcolor) + "\n")

try:
	smtpservercolor=colored("[-]Enter the smtp server : ","green")
	smtpserver=input("{}".format(smtpservercolor))
	smtpportcolor=colored("[-] Enter the smtp port : ","green")
	smtpport=int(input("{}".format(smtpportcolor)))
	usercolor=colored("[-]Enter the username of your smtp : ","green")
	user=input("{}".format(usercolor))
	passwordcolor=colored("[-]Enter the password of your smtp : ","green")
	password=input("{}".format(passwordcolor))
	fromaddresscolor=colored("[-]From your email : ","green")
	fromaddress=input("{}".format(fromaddresscolor))
	toaddresscolor=colored("[-]To victim email : ","green")
	toaddress=input("{}".format(toaddresscolor))
	subjectcolor=colored("[-]Subject : ","green")
	Subject=input("{}".format(subjectcolor))
	messagecolor=colored("[-]Your message : ","green")
	message=input("{}".format(messagecolor))
	messageheadercolor=colored("[-] Enter your header (ex: From: service <m.service@info.org> ) : ","green")
	messageheader=input("{}".format(messageheadercolor))
	sleep(5)
	sendemail=call(" sendemail -s {}:{} -xu {} -xp {} -f '{}' -t '{}' -u '{}' -m '{}' -o message-header='{}' ".format(smtpserver,smtpport,user,password,fromaddress,toaddress,Subject,message,messageheader),shell=True)
	print("\n"+"Done")
except KeyboardInterrupt :
	errorcolor=colored("\n"+"GOODBYE :)","red","on_blue",["bold","blink"])
	print("{}".format(errorcolor))
	