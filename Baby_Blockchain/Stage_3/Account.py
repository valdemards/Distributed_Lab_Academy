import rsa
from Stage_2 import KeyPair


class Account:

    def __init__(self):
        self.account_id = bytes
        self.public_key = rsa.PublicKey
        self.balance = int

    def create_account(self, public_key):
        self.account_id = hash(public_key)
        self.public_key = public_key
        return self

    def update_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def to_string(self):
        account_string = 'id = ' + str(self.account_id) + ' public_key = ' + str(self.public_key) + ' balance = ' + str(self.balance)
        return account_string

    def print(self):
        print('Current balance: ', self.balance)
        print('Public key: ' + self.public_key.save_pkcs1("PEM").decode())


# Creating public key:
key_pair_1 = KeyPair.KeyPair().gen_key_pair()
public_key_1= key_pair_1.public_key

# Creating new account:
test_account = Account().create_account(public_key_1)
test_account.update_balance(5)

# print(test_account.get_balance())
# print(test_account.to_string())
test_account.print()
