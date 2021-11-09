from flask import Flask, request, abort, jsonify
import time
import os, binascii, sqlite3, datetime, inputFilter

app = Flask(__name__)

tokensValidos = {}

class tokenClass():
    def generate_key(self):
        return str(binascii.hexlify(os.urandom(3)).decode())
    
    def verificar_token(self, email, token):
        try:
            banco = sqlite3.connect('tokensDB.db')
            cursor = banco.cursor()
            cursor.execute("SELECT token, data, validade form tokens_senha where email='"+email+"' ORDER BY data DESC")
            res = cursor.fetchone()
            banco.closer()

            data_atual = float(time.mktime(datetime.datetime.now().timetuple()))
            validade = float(res[1])+float(res[2])

            if res[0] == token and data_atual < validade:
                return "True"
            else:
                return "False"
        except:
            return "False"



@app.route('/getMfaCode', methods=['POST'])
def getMfaCodeAPI():
    if not request.json or ('email' and 'usrToken' and 'operacao') not in request.json:
        abort(400)
    email = request.json['email']
    usrToken = request.json['usrToken']
    operacao = request.json['operacao']

    if inputFilter.checkSqlInjection(email):    return "Injeção de SQL detectada.\n"
    if inputFilter.checkSqlInjection(usrToken):    return "Injeção de SQL detectada.\n"
    if inputFilter.checkSqlInjection(operacao):    return "Injeção de SQL detectada.\n"

    tk = tokenClass()

    #Verifica se o token é válido
    if operacao == '0':
        return tk.verificar_token(email, usrToken)
    
    #Gera token
    elif operacao == '1':
        validade = 600 #Validade de 10 minutos em tempo UNIX

        token = ''
        banco = sqlite3.connect('tokensDB.db')
        cursor = banco.cursor()

        token = tk.generate_key().upper()
        cursor.execute("INSERT INTO tokens_senha (email, token, data, validade) VALUES ('"+email+"','"+token+"','"+str(time.mktime(datetime.datetime.now().timetuple()))+"','"+str(validade)+"')")
        banco.commit()
        banco.close()

        return jsonify({'token':token})
    
    else:
        return "Operação inválida"

if __name__ == '__main__':
    app.run(host='192.168.x.x', port=8080, debug=True) #Alterar host para IP do servidor