import rsa

class Signature():

    def signData(private_key, data):
        signature = rsa.sign(data.encode(), private_key, "SHA-256")
        return (signature)

    def verifySignature(signature, data, public_key):
        result = rsa.verify(data.encode(), signature, public_key)
        return(result)

    def toString(signature):
        return f"""{signature}"""

    def printSignature(signature):
        print(signature)


key_pair = rsa.newkeys(1024)
public_key = key_pair[0]
private_key = key_pair[1]
data = 'Hello'
signature = Signature.signData(private_key, data)
print(Signature.verifySignature(signature, data, public_key))
Signature.printSignature(signature)
print(Signature.toString(signature))

