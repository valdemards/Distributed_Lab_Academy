from Stage_2 import KeyPair

class Account:

    def __init__(self):
        self.account_id = bytes
        self.public_keys = []
        self.balance = int

    def create_account(self, public_keys):
        self.account_id = hash(tuple(public_keys))
        self.public_keys = public_keys
        return (self)

    def update_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return(self.balance)

    def to_string(self):
        account_string = 'id = ' + str(self.account_id) + ' keys = ' + str(self.public_keys) + ' balance = ' + str(self.balance)
        return account_string

    def print(self):
        print('Current balance: ', self.balance)
        for key in public_keys:
            print('Public key № {}'.format(public_keys.index(key) + 1) + key.save_pkcs1("PEM").decode())
        # [print(key.save_pkcs1("PEM").decode()) for key in self.public_keys]

# Creating public keys array:
key_pair_1 = KeyPair.KeyPair().gen_key_pair()
key_pair_2 = KeyPair.KeyPair().gen_key_pair()
public_keys = [key_pair_1.public_key, key_pair_2.public_key]

# Creating new account:
test_account = Account().create_account(public_keys)
test_account.update_balance(5)

# print(test_account.get_balance())
# print(test_account.to_string())
# test_account.print()
