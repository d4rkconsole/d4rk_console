#!/bin/python3


import bane  # -Bane credit - Ala
import os
from colorama import Fore , Style
import subprocess
import datetime
import pyfiglet



try:
	import bane
except:
	print(" [!] you need to install bane  [!] " )
	

try:
	import subprocess
except:
	print(" [!] you need to install subprocess module [!] " )

try:
	import os
except:
	print(" [!] you need to install os module [!] " )
 





os.system("clear")

banner = pyfiglet.figlet_format( "   D4RK CONSOLE   " )
print(Fore.BLUE , banner)
print(Fore.RED  + "\t\t\t [+]  Tool Created By -->> D4RK SH4D0W [+]\n\n\t\t [+] A FAILURE PERSON IS MORE INTELLIGENT :) FUCK YOU MY HATERS [+] "  )
print(Style.RESET_ALL)
print("-" * 100)

print(Fore.BLUE + "\n\t\t\t[+] -->> Choose Number Between 1 to 5 [+] \n\t\t\t1 -->> MAC ADDRESS CHANGER\n\t\t\t2 -->> INFORMATION GATHERING\n\t\t\t3 -->> DISCOVER COMPUTER  WHICH ARE CONNECTED TO YOUR SAME NETWORK\n\t\t\t4 -->> Find SUID BIT BINARY FOR PRIVILEGE ESCALATION\n\t\t\t5 -->> FINDING CRONTABS FOR PRIVILEGE ESCALATION  " )
print(Style.RESET_ALL)
print("-" * 100)

no = int(input(Fore.RED + " [+] Enter the Number -->> " ))
	
print(Style.RESET_ALL)
def recon():
	os.system("clear")
	print(Fore.BLUE + "\n\t\t\t [+] Choose Number Between 1 to 4 [+] \n\t\t\t 1 -->> WHOIS_LOOKUP\n\t\t\t 2 -->> SUBDOMAIN_FINDING\n\t\t\t 3 -->> GEO_IP_LOCATION\n\t\t\t 4 -->> WHAT IS YOUR IP LOOKUP\n\t\t\t " )
	number = int(input(" [+] Enter The Number -->> " ))
	if number == 1:
		domain = input(" [+] Enter WEBSITE URL FOR WHOISLOOKUP -->> " )
		print("\t\t\t [+] Doing who is lookup for the website [+] ")
		print("-"* 100)
		b = subprocess.call(["whois" , domain])
		print(b)
	elif  number == 2:
		domain2 = input(" [+] Enter website url to find subdomains -->> " )
		print("\t\t\t [+] FINDING SUBDOMAINS FOR WEBSITE -->> [+] " , domain2)
		print("-"* 100)
		a = subprocess.call(["sublist3r" , "-d" , domain2])
		print(a)
	elif number == 3:
		i = input(" Enter TARGET IP TO FIND ITS GEO LOCATION -->> " )
		print("\t\t\t [+] Finding geo ip location [+] " )
		print("-" * 100)
		c = bane.geoip( i )
		print(c)
	elif number == 4:
		print("\t\t\t FINDING YOUR IP ADDRESS " )
		l1 = bane.myip()
		print("   [+] your currrent ip address is -->> " , l1)
		
	else:
		print("  [!] Please enter the correct number between 1 to 4 [!] ")
print(Style.RESET_ALL)


def mac():
	os.system("clear")
	print(Fore.GREEN + "\t\t [+] You will be anonymous on a network after changing mac address [+]  " )
	
	
			 

	print('-' * 90)
	interface = input(" [+] Enter interface name [ for eg eth0,wlan0 ] -->> " )
	mac = input(" [+] Enter mac address -->> " )
	subprocess.call(["sudo" , "ifconfig" , interface , "down"])
	subprocess.call(["sudo", "ifconfig" , interface , "hw" , "ether" , mac])
	subprocess.call(["sudo" , "ifconfig" , interface , "up"])
	print(" [+] your mac address is changed for interface -->> " , interface )
	print(" [+] your current mac address is -->> " , mac)
	
print(Style.RESET_ALL)

def sh4d0w():
	os.system("clear")
	print(Fore.YELLOW + "\t\t [+] Find COMPUTER ON SAME NETWORK WITH THEIR IP AND MAC ADDRESS [+] " )
	print("-" * 90)
	subnet = input(" [+] Enter your ip address subnet -->> " )
	print("-" * 60)
	print(" [+] Finding computers on same network with ip and mac [+] " )
	subprocess.call(["sudo" , "arp-scan" , subnet])
	print(Style.RESET_ALL)
	


def suid():
	os.system("clear")
	print(Fore.GREEN + "\t\t [+] Finding suid binary for privilege escalation [+] " )
	print("-" * 90)
	print(" [+] Finding suid binary work in progress [+] " )
	print("-" * 60)
	a = subprocess.call(["sudo" , "find" , "/" , "-type" , "f" , "-perm" , "-4000"])
	print(a)
	print(Style.RESET_ALL)
	
	


def crontab():
	os.system("clear")
	print(Fore.YELLOW + "\n\t\t\t [+] Choose Number between 1 and 2 [+]\n\t\t\t1 -->> FIND CRONTAB FOR NORMAL_USER\n\t\t\t2 -->> FIND CRONTAB FOR ROOT USER\n\t\t\t3 -->> FIND CRONTAB USER WHO YOU WANT TO FIND FOR  " )
	print("-" * 100)
	number = int(input(" [+] Enter a Number -->> " ))
	if number == 1:
		print(" [+] Finding crontab for the normal user [+] " )
		print("-" * 70)
		subprocess.call(["sudo" , "crontab" , "-l"])
	elif number == 2:
		print(" [+] Finding crontab for root user [+] " )
		print("-" * 70)
		subprocess.call(["sudo" ,"crontab" , "-u" ,   "root" , "-l"])
	elif number == 3:
		
		print(" [+] Finding crontab for that user which you specfied [+] " )
		print("-" * 80)
		user = str(input( " [+] Enter the user -->> " ))
		subprocess.call(["sudo" , "crontab" , "-u" , user , "-l"])
	else:
		print(" [!] Enter the correct number  [!] " )
		
		
print(Style.RESET_ALL)


		
			
			 
if no == 1:
	mac()
elif no == 2:
	recon()
elif no == 3:
	sh4d0w()
elif no == 4:
	suid()
elif no == 5:
	crontab()
else:
	print( " [!] Please Enter valid number [!] " )

							
	
	

	





  
