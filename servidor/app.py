from flask import Flask, request, abort, jsonify
import time
from time import sleep
from threading import Thread
import os, binascii

app = Flask(__name__)

tokensValidos = {}

class tokenClass():
    def generate_key(self):
        return str(binascii.hexlify(os.urandom(3)).decode())
    
@app.route('/getMfaCode', methods=['POST'])
def getMfaCodeAPI():
    if not request.json or 'matricula' not in request.json:
        abort(400)
    matricula = request.json['matricula']

    x = False
    token = ''

    #Evitando tokens duplicados
    while not x:
        tk = tokenClass()
        token = tk.generate_key().upper()
        if token not in tokensValidos:
            tokensValidos[str(matricula)] = token
            x = True
    
    return jsonify({'token':token})

if __name__ == '__main__':
    app.run(host='192.168.x.x', port=8080, debug=True)