#!/usr/bin/python3
#^^ this won't be needed if you are on Windows, was written for Deb based Linux OS(s)
import random, string,rsa
"""
Very simple script that generates passwords for you and saves it to disk with an associated account
Have done my best to make it as user friendly as I can.
"""
def leng_and_acc():
		tmp_store = []
		passLeng = 0
		try:
			passLeng = int(input("Desired length of the password please: \n:$"))
			if passLeng < 8:
					print("Ah sorry... the password length is not enough!")
		except ValueError:
			passLeng = 8
			print("Defaulting to 8.")
		finally:
			tmp_store.append(passLeng)
		try:
			usr_acc = input("Username(or email) please.\n:$")
		finally:
			tmp_store.append(usr_acc)
		return tmp_store
lengAndAcc = leng_and_acc()
passwd_length = lengAndAcc[0]
usr_name = lengAndAcc[1]
def genPassword(leng):
	chars = string.ascii_letters + string.digits + string.punctuation
	passwd = ""
	for index in range(leng):
		passwd = passwd + random.choice(chars)
	return passwd
print("Just encrypting your data...")
publicKey,privateKey = rsa.newkeys(2048)
passwd = genPassword(passwd_length)
encrypted_passwd = rsa.encrypt(passwd.encode(),publicKey)
encrypted_usr_name = rsa.encrypt(usr_name.encode(),publicKey)
with open("password_store.txt","a") as file:
	file.write(str(encrypted_passwd)+":	")
	file.write(str(encrypted_usr_name)+"\n")
	file.close()
	print("Done...")
	
