# vncdecrypt
VNC password file decryptor

short code to decrypt VNC password files

Usage: ./vncdecrypt.py file

Sample (file taken from HTB)

$ ./vncdecrypt.py ./secret
[*] VNC Password File Decryptor [*]

[*] Opening file:  ./secret
[*] Data read:  b'\xbd\xa8[|\xd5\x96z!'
[*] Decrypted pwd:  VNCP@$$!
