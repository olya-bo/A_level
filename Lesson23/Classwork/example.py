from hashlib import sha256


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_encrypted_password(self):
        return sha256(self.password.encode('utf-8')).hexdigest()

someuser = User(username='Lolo', password='qwerty')
print(someuser.get_encrypted_password())

user = User(username='User', password='qwerty')
user.get_encrypted_password()
print(user.password)