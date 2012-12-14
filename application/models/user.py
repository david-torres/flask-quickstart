from mongoengine import Document
from mongoengine import StringField
import hashlib
import os


class User(Document):
    email = StringField(required=True)
    username = StringField(required=True)
    password = StringField(required=True)

    def set_password(self, password):
        """ Hash password on the fly """
        if isinstance(password, unicode):
            password = password.encode('utf-8')
        password_salt = hashlib.sha1(os.urandom(60)).hexdigest()
        crypt = hashlib.sha1(password + password_salt).hexdigest()
        self.password = unicode(password_salt + crypt, 'utf-8')

    def verify_password(self, password):
        """ Check the password against existing credentials  """
        if isinstance(password, unicode):
            password = password.encode('utf-8')
        password_salt = self.password[:40]
        crypt_pass = hashlib.sha1(password + password_salt).hexdigest()
        if crypt_pass == self.password[40:]:
            return True
        else:
            return False

    def get_id(self):
        return self.email

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False
