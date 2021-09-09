#!/usr/bin/python3
import sys,pyDes

print("[*] VNC Password File Decryptor [*]\n")
if(len(sys.argv)<2) :
	print("[-] File name required.")
	sys.exit(1)

ifile = str(sys.argv[1])
key = [232, 74, 214, 96, 196, 114, 26, 224]

print("[*] Opening file: ",ifile)
with open(ifile,'rb') as fd:
	pwd=fd.read()
	print("[*] Data read: ",pwd)
	des = pyDes.des(key)
	dpwd = des.decrypt(pwd)

	print("[*] Decrypted pwd: ",dpwd.decode("utf-8"))
