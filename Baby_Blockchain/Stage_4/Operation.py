import rsa
from Stage_2 import KeyPair
from Stage_2 import Signature
from Stage_3 import Account


class Operation:

    def __init__(self):
        self.sender = Account.Account()
        self.receiver = Account.Account()
        self.amount = int
        self.signature = bytes

    def create_operation(self, sender, receiver, amount, signature):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature
        return self

    def verify_operation(self, signature, amount):
        try:
            if self.receiver.get_balance() >= amount:
                Signature.Signature().verify_signature(signature, self.receiver.public_key)
            return True
        except Exception as e:
            print(e)
            return False


    def to_string(self):
        operation_string = 'sender = ' + str(self.sender.to_string()) + ' receiver = ' + str(self.receiver.to_string()) + ' amount = ' + str(self.amount) + ' signature = ' + str(self.signature)
        return operation_string

    def print(self):
        print('Sender ', self.sender.to_string())
        print('Receiver ', self.receiver.to_string())
        print('Amount ', self.amount)
        print('Signature ', self.signature)


sender_key_pair = rsa.newkeys(512)
sender_public_key = sender_key_pair[0]
sender_private_key = sender_key_pair[1]

receiver_key_pair = rsa.newkeys(512)
receiver_public_key = receiver_key_pair[0]
receiver_private_key = receiver_key_pair[1]


# Creating new accounts:
sender_account = Account.Account().create_account(sender_public_key)
sender_account.update_balance(1)
receiver_account = Account.Account().create_account(receiver_public_key)
receiver_account.update_balance(0)

amount = 1
# Creating signature:
sender_signature = Signature.Signature.sign_data(sender_private_key, str(amount))

# Tests:

operation_1 = Operation().create_operation(sender_account, receiver_account, amount, sender_signature)
print(operation_1.to_string())
# operation_1.print()
print(operation_1.verify_operation(sender_signature, amount))
