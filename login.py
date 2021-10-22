from sqlite3.dbapi2 import connect
from PyQt5 import  uic,QtWidgets,QtGui, QtCore
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer, QTime, Qt
from PyQt5.QtGui import QGuiApplication
import sqlite3
import hashlib
import pegaHorario
import geoloc
import threading
import time


#class clock(QtCore.QObject):
#
#    def run(self):
#        while(True):
#            hora_atual = pegaHorario.curlHoraStr()
#            pontoT.txtTime.setText(hora_atual)
#            time.sleep(1)


##------ Funções
def relogio():
    #while(True):
        pontoT.txtTime.setText(pegaHorario.curlHoraStr())
        time.sleep(1)

#def atualizaHora(n):
#    pontoT.txtTime.setText(n)

def messageBox(err):
    msgBoxT.loginButton.setText(err)
    msgBoxT.show()

def marcaPonto(matricula):
    try:
        data = pegaHorario.curlFuso()
        utc = pegaHorario.verificarUTC(geoloc.region())

        banco = sqlite3.connect('banco_pontoGP.db') 
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS pontoGP (matricula text,data text,utc text)")
        cursor.execute("INSERT INTO pontoGP VALUES ('"+str(matricula)+"','"+str(data)+"','"+str(utc)+"')")

        banco.commit() 
        banco.close()
        messageBox("Ponto registrado com sucesso.")

    except sqlite3.Error as erro:
        messageBox("Erro ao inserir os dados: "+str(erro))

    pontoT.close()

##------ Telas
def login():
    loginT.error_txt.setText("")
    matricula = loginT.user_mat_log.text()
    senha = loginT.user_pass.text()
    banco = sqlite3.connect('banco_cadastroGP.db') 
    cursor = banco.cursor()
    try:     
        cursor.execute("SELECT senha FROM cadastroGP WHERE matricula ='{}'".format(matricula))
        senha_bd = cursor.fetchall()
        cursor.execute("SELECT admin FROM cadastroGP WHERE matricula = '{}'".format(matricula))
        admVR = cursor.fetchall()
        banco.close()
        if hashlib.sha256(senha.encode('utf-8')).hexdigest() == senha_bd[0][0]:
            if admVR[0][0] == 1:
                loginT.close()
                admT.show() 
                pontoT.pontoButton_2.clicked.connect(lambda: marcaPonto(matricula)) #Declarar dentro da função para não perder o valor da matrícula | ADM View          
            else: 
                loginT.close()
                menuT.show()
                pontoT.pontoButton_2.clicked.connect(lambda: marcaPonto(matricula)) #Declarar dentro da função para não perder o valor da matrícula | USER View
        else:
            loginT.error_txt.setText("Dados de login incorretos!")
    except:
        loginT.error_txt.setText("Erro ao validar o Login")

def reset_confirm():
    reset_confirmT.show()

def recupera_senha():
    matricula = reset_confirmT.user_mat_log.text()
    banco = sqlite3.connect('banco_cadastroGP.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT matricula FROM cadastroGP WHERE matricula = '{}'".format(matricula))
    matriculaVR = cursor.fetchall()
    banco.close()
    if not matriculaVR:
        messageBox("Usuário não encontrado")
        reset_confirmT.close()
        loginT.show()
        return
    
    if matricula == matriculaVR[0][0]:
        reset_confirmT.close()
        reset_alteraT.show()
    else: 
        reset_confirmT.close()
        loginT.show()

#def reset_altera():
#    reset_alteraT.show()

def altera_cadastro(matricula):
    reset_alteraT.show()
    messageBox(str(matricula))
    senha = hashlib.sha256(reset_alteraT.res_newpass.text().encode('utf-8')).hexdigest()
    c_senha = hashlib.sha256(reset_alteraT.res_newpass2.text().encode('utf-8')).hexdigest()


    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastroGP.db') 
            cursor = banco.cursor()
            cursor.execute("UPDATE cadastroGP SET senha WHERE matricula ='{}'".format(matricula))
            banco.commit() 
            banco.close()
            reset_alteraT.status_txt.setText("Usuario cadastrado com sucesso")
            print("Deu certo, passou aqui")

        except sqlite3.Error as erro:
            messageBox("Erro ao inserir os dados: "+str(erro))
        reset_alteraT.close()
        loginT.show()

    else:
        cadT.status_txt.setText("As senhas digitadas estão diferentes")

def chama_cad():
    cadT.show()

def cadastrar():
    nome = cadT.cad_username.text()
    cargo = cadT.cad_func_user.text()
    matricula = cadT.cad_mat_user.text()
    senha = hashlib.sha256(cadT.cad_pass1_log.text().encode('utf-8')).hexdigest()
    c_senha = hashlib.sha256(cadT.cad_pass1_log.text().encode('utf-8')).hexdigest()
    admin = 0

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastroGP.db') 
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastroGP (nome text,cargo text,matricula text,senha text, admin integer)")
            cursor.execute("INSERT INTO cadastroGP VALUES ('"+nome+"','"+cargo+"','"+matricula+"','"+senha+"','"+str(admin)+"')")

            banco.commit() 
            banco.close()
            cadT.cad_return.setText("Usuario cadastrado com sucesso")

        except sqlite3.Error as erro:
            messageBox("Erro ao inserir os dados: "+str(erro))
        cadT.close()
        loginT.show()

    else:
        cadT.cad_return.setText("As senhas digitadas estão diferentes")

    
def telaPonto():
    if geoloc.country() != "Brazil":
        messageBox("Erro: Usuário em região não permitida.")
    else:
        pontoT.show()
        pontoT.txtTime.setText(pegaHorario.curlHoraStr())
        #QtGui.QGuiApplication.processEvents()
        #threading.Thread(target=relogio()).start()
        

## def logout():

app = QtWidgets.QApplication([])
loginT = uic.loadUi("tela_login.ui")
admT = uic.loadUi("tela_adm.ui")
cadT = uic.loadUi("tela_cad.ui")
menuT = uic.loadUi("tela_menu.ui")
pontoT = uic.loadUi("tela_ponto.ui")
msgBoxT = uic.loadUi("tela_messageBox.ui")
reset_confirmT = uic.loadUi("tela_reset_confirm.ui")
reset_alteraT = uic.loadUi("tela_reset_altera.ui")

loginT.loginButton.clicked.connect(login)                                      # Chama Função que verifica Login;
loginT.cadRequest.clicked.connect(chama_cad)                                   # Chama tela de Cadastro;
loginT.user_pass.setEchoMode(QtWidgets.QLineEdit.Password)                     # ;
loginT.resetButton.clicked.connect(reset_confirm)                                 # Chama confirmação de matrícula p/ Reset;

reset_confirmT.resetConfirm.clicked.connect(recupera_senha)
reset_alteraT.resetAltera.clicked.connect(altera_cadastro)

cadT.cadFunc.clicked.connect(cadastrar)                                        # Chama Funcao para cadastrar Colaborador;

menuT.pontoButton.clicked.connect(telaPonto)                                   # Chama tela de Ponto;
admT.pontoButton.clicked.connect(telaPonto)                                    # Chama tela de Ponto;


matricula = ''

loginT.show()
app.exec()