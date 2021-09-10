## _vncdecrypt.py_

[vncdecrypt.py](https://github.com/nikip72/vncdecrypt) stored weak VNC password decryptor

## Usage
```
python3 vncdecrypt.py -i inputfile / -s hex string
```
## Dependencies
[pyDes](https://pypi.org/project/pyDes/) , install with
```
$ sudo pip3 install pyDes
```

## Sample
```
$ ./vncdecrypt.py -i ./com.apple.VNCSettings.txt
VNC Password Decryptor
----------------------
[*] Opening file:  ./com.apple.VNCSettings.txt
[*] Data:  bytearray(b'Gu\x02=\xdc\xe7\x97\xa6\xff\x1c9Vs\x90\xad\xca')
[*] Seems like a native MAC VNC password
[*] Decrypted password:  PASSWORD
$
```

## Obtaining stored VNC passwords
__On [Windows](https://www.microsoft.com)__ (courtesy of [frizb](https://github.com/frizb/PasswordDecrypts))

```
RealVNC
HKEY_LOCAL_MACHINE\SOFTWARE\RealVNC\vncserver
Value: Password
```
```
TightVNC
HKEY_CURRENT_USER\Software\TightVNC\Server
HKLM\SOFTWARE\TightVNC\Server\ControlPassword
tightvnc.ini
vnc_viewer.ini
Value: Password or PasswordViewOnly
```
```
TigerVNC
HKEY_LOCAL_USER\Software\TigerVNC\WinVNC4
Value: Password
```
```
UltraVNC
C:\Program Files\UltraVNC\ultravnc.ini
Value: passwd or passwd2
```

__On [macOS](https://www.apple.com)__
```
Native macOS VNC server
/Library/Preferences/com.apple.VNCSettings.txt
```

__On [Linux](https://www.linux.org)__
```
TightVNC
~/.vnc/passwd
```
