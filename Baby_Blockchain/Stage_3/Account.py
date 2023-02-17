import rsa


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


# with open(r"D:\Trainings\IT\Distributed_Lab_Academy\Distributed_Lab_Academy\Baby_Blockchain\Stage_2\public_key.pem", "rb") as f:
#     public_key = rsa.PublicKey.load_pkcs1((f.read()))
#
# # Creating new account:
# test_account = Account().create_account(public_key)
# test_account.update_balance(5)
#
# # Tests
# print(test_account.get_balance())
# print(test_account.to_string())
# test_account.print()
