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
SHA-256
b"\x12\x05zR\xd7i\x07\xd1\xc0P\x9fPeTr\x87\x04d\xd1'(\xf0\xf1\xac\xea\x80\xcb\xa8\x1e\xc9ljt\xc8i\xddg&od\xfe\xa7r!w\t\xd2\x9b\xad\xf8\x836&o\xf4a#\xae\xeez$2u%"
b"\x12\x05zR\xd7i\x07\xd1\xc0P\x9fPeTr\x87\x04d\xd1'(\xf0\xf1\xac\xea\x80\xcb\xa8\x1e\xc9ljt\xc8i\xddg&od\xfe\xa7r!w\t\xd2\x9b\xad\xf8\x836&o\xf4a#\xae\xeez$2u%"
```


Note : PEP 8 used as a style guide, so classes, methods and parametres naming style, differs from requirement
Please let me know if it is an issue.

