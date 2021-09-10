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
$ python3 vncdecrypt.py -s D7A514D8C556AADE                                                                             VNC Password Decryptor
----------------------
[*] Data:  bytearray(b'\xd7\xa5\x14\xd8\xc5V\xaa\xde')
[*] Decrypted pwd:  Secure!
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

## TODO: add password locations for Mac and Linux
