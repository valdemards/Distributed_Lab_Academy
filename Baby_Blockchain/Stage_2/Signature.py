import rsa


class Signature:

    def sign_data(private_key, data):
        signature = rsa.sign(data.encode(), private_key, "SHA-256")
        return (signature)

    def verify_signature(signature, data, public_key):
        try:
            if isinstance(rsa.verify(data.encode(), signature, public_key), str):
                return True
            else:
                return False
        except:
            return False

    def to_string(signature):
        return f"""{signature}"""

    def print_signature(signature):
        print(signature)


key_pair = rsa.newkeys(512)
public_key = key_pair[0]
private_key = key_pair[1]
data = 'Hello cryptography!'
signature = Signature.sign_data(private_key, data)

print('Testing positive case of verifying signature')
print(Signature.verify_signature(signature, data, public_key))

Signature.print_signature(signature)
print(Signature.to_string(signature))

print('Testing negative case of verifying signature after changing message')
data = 'Good bye cryptography!!'
print(Signature.verify_signature(signature, data, public_key))
