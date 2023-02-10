import rsa

class KeyPair():
    
    def __init__(self):
        key_pair = rsa.newkeys(1024)
        self.__PrivateKey = key_pair[1]
        self.PublicKey = key_pair[0]

    def __repr__(self):
        return f"""{self.__PrivateKey.save_pkcs1(("PEM")).decode()}
{self.PublicKey.save_pkcs1(("PEM")).decode()}"""

new_keypair = KeyPair()
print(new_keypair)