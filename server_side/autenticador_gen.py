from uuid import uuid4
from time import sleep
import os, binascii

def generate_key():
    return str(binascii.hexlify(os.urandom(3)).decode())

#while(True):
#    rand_token = generate_key().upper()
#    print(rand_token)
#    sleep(100)