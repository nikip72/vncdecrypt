#!/usr/bin/python3
import sys,pyDes

def usage():
	print("[-] Usage: ",str(sys.argv[0])," -i raw file / -s hex string")
	sys.exit(1)

def printpwd(s):
	print("[*] Decrypted password: ",s.decode("utf-8"))

print("VNC Password Decryptor")
print("----------------------")
if(len(sys.argv)<3):
	usage()

mode = str(sys.argv[1])

if(mode.lower() == "-i"):
	ifile = str(sys.argv[2])
	print("[*] Opening file: ",ifile)
	with open(ifile,'rb') as fd:
		pwd=fd.read()
	if(len(pwd)==32):
		pwd=bytearray.fromhex(pwd.decode("utf-8"))

elif(mode.lower() == "-s"):
	pwd = bytearray.fromhex(sys.argv[2])

else:
	usage()

print("[*] Data: ",pwd)

if(len(pwd)==8):
	print("[*] Seems like a native VNC password")
	key = [232, 74, 214, 96, 196, 114, 26, 224]
	des = pyDes.des(key)
	dpwd = des.decrypt(pwd)
	printpwd(dpwd)

elif(len(pwd)==16 and pwd[14]==0xAD and pwd[15]==0xCA):
	print("[*] Seems like a native MAC VNC password")
	kb=bytearray.fromhex("1734516E8BA8C5E2FF1C39567390ADCA")
	dpwd = bytes(a ^ b for (a, b) in zip(kb, pwd))
	printpwd(dpwd)

else:
	print("[-] Unrecognized format.")
