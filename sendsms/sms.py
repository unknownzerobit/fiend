from selenium import webdriver
from subprocess import call
from termcolor import colored
from time import sleep
print('''
			        
			███████╗██╗███████╗███╗   ██╗██████╗ 
			██╔════╝██║██╔════╝████╗  ██║██╔══██╗
			█████╗  ██║█████╗  ██╔██╗ ██║██║  ██║
			██╔══╝  ██║██╔══╝  ██║╚██╗██║██║  ██║
			██║     ██║███████╗██║ ╚████║██████╔╝
			╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ 
	                                                ''')

#user input
try:
	startcolor=colored("\n"+"########## Please don't use it as evil purposes if don't work in your country please use fast vpn  ########## " ,"blue")
	print("{}".format(startcolor) + "\n")
	sleep(3)
	usercolor=colored("[*] Enter your username(for clicksend service) : ","green")
	user=input("{}".format(usercolor))
	passwordcolor=colored("[*] Enter your password(for clicksend service ) : ","green")
	password=input("{}".format(passwordcolor))
	numcolor=colored("[*] Enter number of victem with country code : ","green")
	phone=int(input("{}".format(numcolor)))
	smscolor=colored("[*] type your sms message Please note that it should be 160 characters only : ","green")
	sms=input("{}".format(smscolor))
	color_delay=colored("[*]Enter the delay(Recommended 60 second or more): ","green")
	delay=input("{}".format(color_delay))
	print('\n' + "Please wait ......")
except KeyboardInterrupt:
                         x=colored("GOODBYE :)","red","on_blue",["bold","blink"])
                         print('\n' + "{}".format(x))
                         exit()	


#login page 

driver=webdriver.Firefox()
driver.get("https://dashboard.clicksend.com/login")
try:
	try:
		    username=driver.find_element_by_class_name("form-control").send_keys("{}".format(user))
		    password=driver.find_element_by_class_name("form-control-appended").send_keys("{}".format(password))
		    sleep(8)
		    signin=driver.find_element_by_class_name("btn-clicksend-blue").click()
		    sleep(int(delay))
		   
	except Exception :
	                  invaild_color=colored("[!] Same thing invaild","red","on_blue",["bold","blink"])
	                  print("{}".format(invaild_color))
	                  exit()
# send sms page
	try: 
		
		sms_path=driver.find_element_by_id("sms_li").click()
		sms_xpath=driver.find_element_by_xpath("//a[@href='#/sms/send-sms/main']").click()
		sleep(5)
		victem_num=driver.find_element_by_css_selector('#searchInput').send_keys("{}".format(phone))
		sms_message=driver.find_element_by_id("input_1").send_keys("{}".format(sms))
		sendsms=driver.find_element_by_xpath("//button[@class='btn btn-primary ng-binding']").click()
		sleep(4)
		send=driver.find_element_by_xpath("//button[@class='btn btn-success form-control sms_sendbtn']").click()
		sleep(7)
		driver.close()
		done=colored("[✓✓] The message has been sent sucessfully\nGOODBYE :) ","green")
		print("{}".format(done))

	
	except:
		   invaild_color=colored("[!] Same thing invaild","red","on_blue",["bold","blink"])
		   print("{}".format(invaild_color))
		   exit()

except KeyboardInterrupt:
                         x=colored("GOODBYE :)","red","on_blue",["bold","blink"])
                         print("{}".format(x))
                         exit()
