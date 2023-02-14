Within stage 3 "Baby Blockchain task" I created Account class, almost according to task requirements.
The only one difference is, that every account can have only 1 key_pair, because every voter will have only one 
verified account.
update_balance() function will be updated later, after Node class implementation. Only Node class objects will
have permissions for updating accounts balance.

print(test_account.get_balance()):
```
C:\Python310\python.exe D:/Trainings/IT/Distributed_Lab_Academy/Distributed_Lab_Academy/Baby_Blockchain/Stage_3/Account.py
5

Process finished with exit code 0
```

print(test_account.to_string())
```
C:\Python310\python.exe D:/Trainings/IT/Distributed_Lab_Academy/Distributed_Lab_Academy/Baby_Blockchain/Stage_3/Account.py
id = -3634083748892633486 public_key = PublicKey(16396969348620787835955505706500250522444904168685522958228130146483567396795118188443770587239743319516350763555165086178535452397896922607989477063516798995729770533733138706289013143505285051808463760657768008156471003765365558834906321490267789989557348060955527645585720859523599643150798090881069984088835352575998901039899156967894305541415060590526089563337805099484630323365300193192693721707296464731138772742211696933963839296367586030027484204874172450411636726249926596943287086732262604732010425769567987980903511699252276146815716412481007104153013193670655049371873564015016855198363379537605884366519, 65537) balance = 5

Process finished with exit code 0
```

test_account.print()
```
C:\Python310\python.exe D:/Trainings/IT/Distributed_Lab_Academy/Distributed_Lab_Academy/Baby_Blockchain/Stage_3/Account.py
Current balance:  5
Public key: -----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAiFbPTa04gt6hTNzxQeuOvQTD43Ln+75fYvYF4OEG8eIkbKW9VIRW
8khc6snnKFr3A7N2gg3tOzvZJTUVHqG5k/xDyO77HEccwkXCMwX/5dAzLV8/St15
phEZjJJQ/AzLwsfSIDzEHFJlAIgQ4vTddTOwVWd9dyF/s60WrDJYTVKYO5f+hwZ7
gPUUbPrsJlJFOEGbpy7JoM7z1narJpABNenSGTYy7Zv50xvmsR4Ik95gxwuzMwXM
zwNjwWj/WEgN6FOZTN3OUbEhCkaMr8BlOQpBuRtLoOpsOkXCoW2DjkyR5in0RIDz
mOpOabC2KMnit3qzKri4y7hCksYdx6Hv4QIDAQAB
-----END RSA PUBLIC KEY-----


Process finished with exit code 0

```
