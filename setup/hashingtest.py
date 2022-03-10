from email import message
from getpass import getpass
import hashlib
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import getpass


def main() -> None:
    # a = hash("Baum")
    # print(a)
    # b = hash("Haus")
    # if b == a:
    #     print("Der Code ist korrekt")
    # else:
    #     print("Der Code ist nicht korrekt")    

    # hash_object = "65bc0e830702ad8e5c1da3172591dd2b"

    # test_object = hashlib.md5(b"haus")
    # print(test_object.hexdigest())

    # if  test_object.hexdigest() == hash_object:
    #     print("Der Code ist korrekt")
    # else:
    #     print("Der Code ist nicht korrekt")

    # key = Fernet.generate_key()
    # f = Fernet(key)
    # print(f)

    # token = f.encrypt(b"Gude")
    # print(token)
    # d = f.decrypt(token)

    # print(d)

    
    
    # password = getpass.getpass(prompt="Passwort: ", stream=None)
    # s = b"hallo"
    # kdf = PBKDF2HMAC(
    #     algorithm=hashes.SHA256(),
    #     length=32,
    #     salt=s,
    #     iterations=390000
    # )
    # key = base64.urlsafe_b64encode(kdf.derive(bytes(password, encoding="ascii")))
    # f = Fernet(key)

    # # message=b"cppsecret.com"
    # # enc = f.encrypt(message)
    # # dec = f.decrypt(enc)
    # tmp = b'gAAAAABiKEx4yx_mFLhWeHxvcB7cVFqU4jazDAHcJGKZzm_WH1Pm8B_2r6Fm2A7Hl1SySEfNEE_0wajtc4vsmHMo4sCEz36Ixw=='
    # print(f.decrypt(tmp))
    # print("Decrypted message: ",dec)
    # print("Encrypted message: ",enc)

    # class AutoKlasse():
    #     def __init__(self, farbe, marke):
    #         self.farbe = farbe
    #         self.marke = marke
    #     def tut_fahren(self):
    # Auto1 = AutoKlasse("Rot", "Corsa")
    # print(Auto1.farbe)
    # Auto1.tut_fahren(4)




if __name__ == '__main__':
    main()
    