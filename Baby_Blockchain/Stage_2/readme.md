Within stage 2 "Baby Blockchain task" I created KeyPair and Signature classes, according to task requirements, using python and rsa library (pip3 install rsa).

Results of running KeyPair.py:
```
C:\Python310\python.exe D:/Trainings/IT/Distributed_Lab_Academy/Distributed_Lab_Academy/Baby_Blockchain/Stage_2/KeyPair.py
-----BEGIN RSA PUBLIC KEY-----
MAoCAwCBZwIDAQAB
-----END RSA PUBLIC KEY-----

-----BEGIN RSA PRIVATE KEY-----
MCQCAQACAwCBZwIDAQABAgJ4cQICANMCAgCdAgIArQIBZQICAKg=
-----END RSA PRIVATE KEY-----

-----BEGIN RSA PRIVATE KEY-----
MCQCAQACAwCBZwIDAQABAgJ4cQICANMCAgCdAgIArQIBZQICAKg=
-----END RSA PRIVATE KEY-----

-----BEGIN RSA PUBLIC KEY-----
MAoCAwCBZwIDAQAB
-----END RSA PUBLIC KEY-----


Process finished with exit code 0
```

Results of running Signature.py:
```
C:\Python310\python.exe D:/Trainings/IT/Distributed_Lab_Academy/Distributed_Lab_Academy/Baby_Blockchain/Stage_2/Signature.py
Testing positive case of verifying signature
True
b'2=\xbf\xd2\xe9jp\xe45aA<3\x85R\xc1\x02@{\xed\xac\xc4`XP\xba!\xc2\x0b\xb1[\x05\xb0\xd1\'\xcbe#\x85mv\xb7"\xe8\x91\xf1ny!\xb6\xc4o\xfe.\x8c\xc1\xe2\xf1\xf8p\xf4\x90Sr'
b'2=\xbf\xd2\xe9jp\xe45aA<3\x85R\xc1\x02@{\xed\xac\xc4`XP\xba!\xc2\x0b\xb1[\x05\xb0\xd1\'\xcbe#\x85mv\xb7"\xe8\x91\xf1ny!\xb6\xc4o\xfe.\x8c\xc1\xe2\xf1\xf8p\xf4\x90Sr'
Testing negative case of verifying signature after changing message
False

Process finished with exit code 0

```


Note : PEP 8 used as a style guide, so classes, methods and parametres naming style, differs from requirement
Please let me know if it is an issue.

