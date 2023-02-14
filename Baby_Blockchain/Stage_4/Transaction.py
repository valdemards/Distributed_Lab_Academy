import rsa
from Stage_2 import KeyPair
from Stage_2 import Signature
from Stage_3 import Account
from Stage_4 import Operation

class Transaction:

    def __init__(self):
        self.initiator = Account.Account().account_id
        self.operations = [Operation.Operation()]
        self.nonce = int

    def create_transaction(self, initiator, operations):
        self.initiator = initiator
        self.operations = operations
        self.nonce = hash(tuple(operations)) + hash(initiator)
        return self

    def to_string(self):
        transaction_string = 'initiator = ' + self.initiator.to_string() + ' operations = ' + ''.join(operation.to_string() for operation in self.operations) + ' nonce = ' + str(self.nonce)
        return transaction_string

    def print(self):
        print('Initiator ', self.initiator.to_string())
        print('Operations ', ''.join(operation.to_string() for operation in self.operations))
        print('Nonce ', self.nonce)


sender_key_pair = rsa.newkeys(512)
sender_public_key = sender_key_pair[0]
sender_private_key = sender_key_pair[1]
sender_account = Account.Account().create_account(sender_public_key)
sender_account.update_balance(1)

receiver_key_pair_1 = rsa.newkeys(512)
receiver_public_key_1 = receiver_key_pair_1[0]
receiver_private_key_1 = receiver_key_pair_1[1]
receiver_account_1 = Account.Account().create_account(receiver_public_key_1)
receiver_account_1.update_balance(0)

receiver_key_pair_2 = rsa.newkeys(512)
receiver_public_key_2 = receiver_key_pair_2[0]
receiver_private_key_2 = receiver_key_pair_2[1]
receiver_account_2 = Account.Account().create_account(receiver_public_key_2)
receiver_account_2.update_balance(0)
# Creating new accounts:

amount = 1
# Creating signature:
sender_signature = Signature.Signature.sign_data(sender_private_key, str(amount))

# Tests:
operation_1 = Operation.Operation().create_operation(sender_account, receiver_account_1, amount, sender_signature)
operation_2 = Operation.Operation().create_operation(sender_account, receiver_account_2, amount, sender_signature)

operations = [operation_1, operation_2]
transaction_1 = Transaction().create_transaction(sender_account, operations)

print(transaction_1.to_string())
transaction_1.print()