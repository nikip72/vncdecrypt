#!/usr/bin/python3
import sys,pyDes

def usage():
	print("[-] Usage: ",str(sys.argv[0])," -i file / -s hex string")

key = [232, 74, 214, 96, 196, 114, 26, 224]
print("VNC Password Decryptor")
print("----------------------")
if(len(sys.argv)<3):
	usage()
	sys.exit(1)

mode = str(sys.argv[1])

if(mode.lower() == "-i"):
	ifile = str(sys.argv[2])
	print("[*] Opening file: ",ifile)
	with open(ifile,'rb') as fd:
		pwd=fd.read()

elif(mode.lower() == "-s"):
	pwd = bytearray.fromhex(sys.argv[2])

else:
	usage()
	sys.exit(1)

print("[*] Data: ",pwd)
des = pyDes.des(key)
dpwd = des.decrypt(pwd)

print("[*] Decrypted pwd: ",dpwd.decode("utf-8"))
