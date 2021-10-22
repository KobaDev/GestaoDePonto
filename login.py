from sqlite3.dbapi2 import connect
from PyQt5 import  uic,QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
import sqlite3
import hashlib
import pegaHorario
import geoloc
import threading
import time

class Worker(QObject):
    updateDate = pyqtSignal()
    trigger = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(Worker, self).__init__(*args, **kwargs)

    def attData(self):
        Win.pontoT.txtTime.setText(pegaHorario.curlHoraStr())

    def relogio(self):
        self.updateDate.connect(self.attData)
        while(True):
            time.sleep(1)
            self.updateDate.emit()

class Win():
    app = QtWidgets.QApplication([])
    wk = Worker()

    loginT = uic.loadUi("tela_login.ui")
    admT = uic.loadUi("tela_adm.ui")
    cadT = uic.loadUi("tela_cad.ui")
    menuT = uic.loadUi("tela_menu.ui")
    pontoT = uic.loadUi("tela_ponto.ui")
    msgBoxT = uic.loadUi("tela_messageBox.ui")
    reset_confirmT = uic.loadUi("tela_reset_confirm.ui")
    reset_alteraT = uic.loadUi("tela_reset_altera.ui")

    def __init__(self):
        super(Win, self).__init__()

    def messageBox(err):
        Win.msgBoxT.loginButton.setText(err)
        Win.msgBoxT.show()

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
            Win.messageBox("Ponto registrado com sucesso.")

        except sqlite3.Error as erro:
            Win.messageBox("Erro ao inserir os dados: "+str(erro))

        Win.pontoT.close()

    ##------ Telas
    def login():
        matricula = Win.loginT.user_mat_log.text()
        senha = Win.loginT.user_pass.text()
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
                    Win.loginT.close()
                    Win.admT.show() 
                    Win.pontoT.pontoButton_2.clicked.connect(lambda: Win.marcaPonto(matricula)) #Declarar dentro da função para não perder o valor da matrícula | ADM View          
                else: 
                    Win.loginT.close()
                    Win.menuT.show()
                    Win.pontoT.pontoButton_2.clicked.connect(lambda: Win.marcaPonto(matricula)) #Declarar dentro da função para não perder o valor da matrícula | USER View
            else:
                Win.loginT.error_txt.setText("Dados de login incorretos!")
        except:
            Win.loginT.error_txt.setText("Erro ao validar o Login")

    def reset_confirm():
        Win.reset_confirmT.show()

    def recupera_senha(matricula):
        banco = sqlite3.connect('banco_cadastroGP.db') 
        cursor = banco.cursor()
        cursor.execute("SELECT matricula FROM cadastroGP WHERE matricula = '{}'".format(matricula))
        matriculaVR = cursor.fetchall()
        banco.close()
        if not matriculaVR:
            Win.messageBox("Usuário não encontrado")
            Win.reset_confirmT.close()
            Win.loginT.show()
            return
        
        if matricula == matriculaVR[0][0]:
            Win.reset_confirmT.close()
            Win.reset_alteraT.show()
        else: 
            Win.reset_confirmT.close()
            Win.loginT.show()

    #def reset_altera():
    #    reset_alteraT.show()

    def altera_cadastro(matricula):
        matricula = Win.reset_confirmT.user_mat_log.text()
        Win.reset_alteraT.show()
        senha = hashlib.sha256(Win.reset_alteraT.res_newpass.text().encode('utf-8')).hexdigest()
        c_senha = hashlib.sha256(Win.reset_alteraT.res_newpass2.text().encode('utf-8')).hexdigest()


        if (senha == c_senha):
            try:
                banco = sqlite3.connect('banco_cadastroGP.db') 
                cursor = banco.cursor()
                cursor.execute("UPDATE cadastroGP SET senha = '"+senha+"' WHERE matricula = '{}'".format(matricula))
                banco.commit() 
                banco.close()
                Win.messageBox("Usuario atualizado com sucesso")

            except sqlite3.Error as erro:
                Win.messageBox("Erro ao inserir os dados: "+str(erro))

            Win.reset_alteraT.close()
            Win.loginT.show()

        else:
            Win.messageBox("As senhas digitadas estão diferentes")

    def chama_cad():
        Win.cadT.show()

    def cadastrar():
        nome = Win.cadT.cad_username.text()
        cargo = Win.cadT.cad_func_user.text()
        matricula = Win.cadT.cad_mat_user.text()
        senha = hashlib.sha256(Win.cadT.cad_pass1_log.text().encode('utf-8')).hexdigest()
        c_senha = hashlib.sha256(Win.cadT.cad_pass1_log.text().encode('utf-8')).hexdigest()
        admin = 0

        if (senha == c_senha):
            try:
                banco = sqlite3.connect('banco_cadastroGP.db') 
                cursor = banco.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS cadastroGP (nome text,cargo text,matricula text,senha text, admin integer)")
                cursor.execute("INSERT INTO cadastroGP VALUES ('"+nome+"','"+cargo+"','"+matricula+"','"+senha+"','"+str(admin)+"')")

                banco.commit() 
                banco.close()
                Win.cadT.cad_return.setText("Usuario cadastrado com sucesso")

            except sqlite3.Error as erro:
                Win.messageBox("Erro ao inserir os dados: "+str(erro))
            Win.cadT.close()
            Win.loginT.show()

        else:
            Win.cadT.cad_return.setText("As senhas digitadas estão diferentes")

        
    def telaPonto():
        if geoloc.country() != "Brazil":
            Win.messageBox("Erro: Usuário em região não permitida.")
        else:
            Win.pontoT.show()
            Win.pontoT.txtTime.setText(pegaHorario.curlHoraStr())
            #QtGui.QGuiApplication.processEvents()
            threading.Thread(target=Win.wk.relogio).start()
            
    loginT.loginButton.clicked.connect(login)                                      # Chama Função que verifica Login;
    loginT.cadRequest.clicked.connect(chama_cad)                                   # Chama tela de Cadastro;
    loginT.user_pass.setEchoMode(QtWidgets.QLineEdit.Password)                     # ;
    loginT.resetButton.clicked.connect(reset_confirm)                              # Chama confirmação de matrícula p/ Reset;

    reset_confirmT.resetConfirm.clicked.connect(lambda: Win.recupera_senha(Win.reset_confirmT.user_mat_log.text()))
    reset_alteraT.resetAltera.clicked.connect(altera_cadastro)

    cadT.cadFunc.clicked.connect(cadastrar)                                        # Chama Funcao para cadastrar Colaborador;

    menuT.pontoButton.clicked.connect(telaPonto)                                   # Chama tela de Ponto;
    admT.pontoButton.clicked.connect(telaPonto)

    loginT.show()




## variaveis:
matricula = ''
Win.app.exec()