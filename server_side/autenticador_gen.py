from uuid import uuid4
from time import sleep
import os, binascii

def generate_key():
    return str(binascii.hexlify(os.urandom(3)).decode())

def gerador_token_short_ttl():
    while(True):
        rand_token = generate_key().upper()
        print(rand_token)
        sleep(100)