import rsa

class KeyPair():

    def __init__(self):
        self.PublicKey = rsa.PublicKey
        self.__PrivateKey = rsa.PrivateKey

    def genKeyPair(self):
        key_pair = rsa.newkeys(16)
        self.PublicKey = key_pair[0]
        self.__PrivateKey = key_pair[1]
        return (self)

    def printKeyPair(self):
        print(self.PublicKey.save_pkcs1(("PEM")).decode())
        print(self.__PrivateKey.save_pkcs1(("PEM")).decode())

    def toString(self):
        return f"""{self.__PrivateKey.save_pkcs1(("PEM")).decode()}
{self.PublicKey.save_pkcs1(("PEM")).decode()}"""


new_keypair = KeyPair().genKeyPair()
new_keypair.printKeyPair()
print(new_keypair.toString())