######################################################################################
##             NOVO LOGIN.PY (ACOMPANHANDO NOVA INTERFACE E MODULANDO)
# Programa desenvolvido como atividade avaliativa pelos alunos: 
#       Bianca Mancini, Jadson Nascimento, Renato Kobashigawa e Marcelo Santana
######################################################################################

######################################################################################
##                                  IMPORTS
######################################################################################

################################################################
## RECURSO PARA CONEXÃO COM O BANCO DE DADOS
################################################################
from sqlite3.dbapi2 import connect
import sqlite3

################################################################
## RECURSO PARA INTERAÇÃO COM INTERFACE GRÁFICA
################################################################
from PyQt5 import  uic,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from ui_tela_menu import Ui_MainWindow


################################################################
## RECURSO PARA CRIPTOGRAFIA | THREADING | TIME
################################################################
from PyQt5.QtCore import pyqtSignal, QObject
import hashlib
import threading
import time
import sys, os


################################################################
## RECURSO INTERNOS CRIADOS PELOS ALUNOS
################################################################
import pega_horarioGP
import geolocGP
import ui_tela_menu

#import envia_emailGP
#import auth_genGP

######################################################################################
########        INTEGRANDOS TELAS À VARIÁVEIS QUE IREMOS CHAMAR POSTERIORMENTE
######################################################################################




class Worker(QObject):
    updateDate = pyqtSignal()
    trigger = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(Worker, self).__init__(*args, **kwargs)

    def attData(self):
        Win.tela_menu.lbl_data.setText(pega_horarioGP.curlSomenteHoraStr())

    def relogio(self):
        self.updateDate.connect(self.attData)
        while(True):
            time.sleep(1)
            self.updateDate.emit()

class Win():
    app = QtWidgets.QApplication([])
    wk = Worker()

    tela_cadastro = uic.loadUi("tela_cadastro.ui")
    tela_login = uic.loadUi("tela_login.ui")
    tela_menu = uic.loadUi("tela_menu.ui")
    tela_messageBox = uic.loadUi("tela_messageBox.ui")
    #tela_menu_adm = uic.loadUi("tela_adm.ui")  - Tela ainda não foi desenhada;
    tela_resete_confirma = uic.loadUi("tela_reset_confirm.ui")
    tela_resete_altera = uic.loadUi("tela_reset_altera.ui")
    #tela_ponto = uic.loadUi("tela_ponto.ui")   - Comentado, pois precisará recodar;
    #tela_messageBox = uic.loadUi("tela_messageBox.ui") - Comentado, pois precisará recodar;
    

    ######################################################################################
    # Telas | Funções e chamadas
    ######################################################################################

    ######################################################################################
    ##                                     FUNÇÕES
    ######################################################################################
    
    def __init__(self):
            super(Win, self).__init__()
          

    def messageBox(err):
            Win.tela_messageBox.txtMsg.setText(err)
            Win.tela_messageBox.show()

    def marcaPonto(matricula):      ##  FUNCIONAL, MAS PRECISAMOS MELHORAR A FORMA DE AMAZENAS A INFORMAÇÃO | NOME também precisa regastar da cadastraGP
        try:
            data = pega_horarioGP.curlFuso()
            utc = pega_horarioGP.verificarUTC(geolocGP.region())

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

    ######################################################################################
    ##                                      TELAS
    ######################################################################################

    ##################################
    # Telas | LOGIN
    ##################################

    def login():
        user_email = Win.tela_login.user_login_edt.text()
        senha = Win.tela_login.user_password_edt.text()
        banco = sqlite3.connect('banco_cadastroGP.db') 
        cursor = banco.cursor()
        try:     
            cursor.execute("SELECT senha FROM cadastroGP WHERE user_email ='{}'".format(user_email))
            senha_bd = cursor.fetchone()
            cursor.execute("SELECT admin FROM cadastroGP WHERE user_email = '{}'".format(user_email))
            admVR = cursor.fetchone()
            if hashlib.sha256(senha.encode('utf-8')).hexdigest() == senha_bd[0]:
                if admVR[0] == 1: 
                    try:
                        Win.tela_login.close()
                        banco.close()
                        #Win.tela_menu_adm.show()       ## UI da tela de ADM, ainda não foi criada!!!
                        #Win.tela_ponto.pontoButton_2.clicked.connect(lambda: Win.marcaPonto(matricula)) #Declarar dentro da função para não perder o valor da matrícula | ADM View 
                    except ValueError as err:
                        Win.messageBox(err)         
                else: 
                    try:
                        Win.tela_login.close()
                        cursor.execute("SELECT primeiro_nome, segundo_nome, cargo, matricula, user_email FROM cadastroGP WHERE user_email ='{}'".format(user_email))
                        content_bd = cursor.fetchone()
                        banco.close()
                        Win.tela_menu.show()
                        Win.tela_menu.lbl_nome.setText(content_bd[0]+" "+content_bd[1])
                        Win.tela_menu.lbl_cargo.setText(content_bd[2])
                        Win.tela_menu.lbl_matricula.setText(content_bd[3])
                        Win.tela_menu.lbl_email.setText(content_bd[4])
                        #Win.pontoT.pontoButton_2.clicked.connect(lambda: Win.marcaPonto(matricula)) #Declarar dentro da função para não perder o valor da matrícula | USER View
                    except ValueError as err:
                        Win.messageBox(err)
                        
            else:
                Win.messageBox("Dados de login incorretos!")
        except:
            Win.messageBox("Erro ao validar o Login")

    ##################################
    # Telas | CADASTRO
    ##################################
    def chama_cad():
        Win.tela_cadastro.show()

    def cadastrar():
        primeiro_nome = Win.tela_cadastro.primeiro_nome_edt.text()
        segundo_nome = Win.tela_cadastro.segundo_nome_edt.text()
        user_email = Win.tela_cadastro.user_email_edt.text()
        senha = hashlib.sha256(Win.tela_cadastro.user_password_edt.text().encode('utf-8')).hexdigest()
        c_senha = hashlib.sha256(Win.tela_cadastro.user_password2_edt.text().encode('utf-8')).hexdigest()
        admin = 0
        matricula = "n/a"
        cargo = "n/a"

        if (senha == c_senha):
            try:
                banco = sqlite3.connect('banco_cadastroGP.db') 
                cursor = banco.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS cadastroGP (primeiro_nome text,segundo_nome text,user_email text,senha text, admin integer,cargo text,matricula text)")
                cursor.execute("INSERT INTO cadastroGP VALUES ('"+primeiro_nome+"','"+segundo_nome+"','"+user_email+"','"+senha+"','"+str(admin)+"','"+cargo+"','"+matricula+"')")

                banco.commit() 
                banco.close()
                Win.tela_cadastro.cadastra_func_btn.setText("Usuario cadastrado com sucesso")

            except sqlite3.Error as erro:
                Win.messageBox("Erro ao inserir os dados: "+str(erro))
            Win.tela_cadastro.close()
            Win.tela_login.show()

        else:
            Win.tela_cadastro.cad_return.setText("As senhas digitadas estão diferentes")
    
    ##################################
    # Telas | RESET CONFIRM - CONSTRUINDO (NÃO LINKADO)
    ##################################     

    def reset_confirm():
        Win.tela_resete_confirma.show()

    def recupera_senha(user_email):
        banco = sqlite3.connect('banco_cadastroGP.db') 
        cursor = banco.cursor()
        cursor.execute("SELECT user_email FROM cadastroGP WHERE user_email = '{}'".format(user_email))
        user_emailVR = cursor.fetchone()
        banco.close()
        if not user_emailVR:
            print("Chegou na condição de encontrar usuário no banco")
            #Win.messageBox("Usuário não encontrado")
            Win.tela_resete_confirma.close()
            Win.tela_login.show()
            return
        
        if user_email == user_emailVR[0]:
            Win.tela_resete_confirma.close()
            Win.tela_resete_altera.show()
        else: 
            Win.tela_resete_confirma.close()
            Win.tela_login.show()

    ##################################
    # Telas | RESETE ALTERA- CONSTRUINDO (NÃO LINKADO)
    ##################################    

    def altera_cadastro(user_email):
        user_email = Win.tela_resete_confirma.user_email_edt.text()
        Win.tela_resete_altera.show()
        #codigo_seg = Win.tela_resete_altera.codigo_edt.text()      -   Não implmentado no código, precisa criar nuva função de verificação e criar animação da UI.
        senha = hashlib.sha256(Win.tela_resete_altera.user_password_edt.text().encode('utf-8')).hexdigest()
        c_senha = hashlib.sha256(Win.tela_resete_altera.user_password2_edt.text().encode('utf-8')).hexdigest()

        
        if (senha == c_senha):
            try:
                banco = sqlite3.connect('banco_cadastroGP.db') 
                cursor = banco.cursor()
                cursor.execute("UPDATE cadastroGP SET senha = '"+senha+"' WHERE user_email = '{}'".format(user_email))
                banco.commit() 
                banco.close()
                Win.messageBox("Usuario atualizado com sucesso")

            except sqlite3.Error as erro:
                Win.messageBox("Erro ao inserir os dados: "+str(erro))

            Win.tela_resete_altera.close()
            Win.tela_login.show()

        else:
            Win.messageBox("As senhas digitadas estão diferentes")
    
    ##################################
    # Telas | MENU - CONSTRUIINDO
    ##################################
    def mainwindow(self):
        main_win = Win.MainWindow()
        return main_win


    class MainWindow(QMainWindow):
        def __init__(self):
            self.main_win = QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.main_win)

            self.ui.stackedWidget.setCurrentWidget(self.ui.main_pg)
            ## BOTÕES DA TOOLBAR ##
            self.ui.home_btn.clicked.connect(self.main_pg)
            self.ui.sair_btn.clicked.connect(self.sair)

            ## PAGINA DE DADOS ##
            self.ui.meus_dados1_btn.clicked.connect(self.data_view_pg)
            self.ui.meus_dados2_btn.clicked.connect(self.data_view_pg)
            self.ui.data_edit_btn.clicked.connect(self.data_change_pg1)
            self.ui.data_alterar_senha_btn.clicked.connect(self.data_change_pg2)
            self.ui.data_salvar_btn1.clicked.connect(self.main_pg)
            self.ui.data_salvar_btn2.clicked.connect(self.main_pg)

            ## PAGINA DE MARCA PONTO ##
            self.ui.marcaponto_btn1.clicked.connect(self.user_marcaponto_pg)
            self.ui.marcaponto_btn2.clicked.connect(self.user_marcaponto_pg1)

            ## PAGINA DE RELATORIO ##
            self.ui.relatorio_btn1.clicked.connect(self.relatorio_fr_pg)
            self.ui.relatorio_btn2.clicked.connect(self.relatorio_fr_pg)

        
    def show():
        Win.main_win.show()

    def main_pg():
        Win.tela_menu.stackedWidget.setCurrentWidget(Win.tela_menu.main_pg)

    def data_view_pg():
        Win.tela_menu.stackedWidget.setCurrentWidget(Win.tela_menu.data_view_pg)

    def data_change_pg1():
        Win.tela_menu.stackedWidget.setCurrentWidget(Win.tela_menu.data_change_pg1)

    def data_change_pg2():
        Win.tela_menu.stackedWidget.setCurrentWidget(Win.tela_menu.data_change_pg2)

    def user_marcaponto_pg():
        Win.tela_menu.stackedWidget.setCurrentIndex(0)
    def user_marcaponto_pg1():
        Win.tela_menu.stackedWidget.setCurrentIndex(1)
    def user_marcaponto_pg2():
        Win.tela_menu.stackedWidget.setCurrentIndex(2)
    def user_marcaponto_pg3():
        Win.tela_menu.stackedWidget.setCurrentIndex(3)
    def user_marcaponto_pg4():
        Win.tela_menu.stackedWidget.setCurrentIndex(4)
        Win.tela_menu.lbl_dia.setText(pega_horarioGP.curlDiaSemanaStr()+", "+pega_horarioGP.curlDiaStr())
        Win.tela_menu.lbl_data.setText(pega_horarioGP.curlSomenteHoraStr())
        threading.Thread(target=Win.wk.relogio).start()
    def user_marcaponto_pg5():
        Win.tela_menu.stackedWidget.setCurrentIndex(5)
    
    def sair():
        os._exit(1)

 

    ##################################
    # Telas | ?? Editável - CONSTRUIINDO
    ##################################

    ######################################################################################
    
    tela_login.login_btn.clicked.connect(login)                                      # Chama Função que verifica Login;
    tela_login.cadastra_btn.clicked.connect(chama_cad)                               # Chama tela de Cadastro;
    tela_login.user_password_edt.setEchoMode(QtWidgets.QLineEdit.Password)           # ;
    tela_login.recupera_btn.clicked.connect(reset_confirm)                           # Chama confirmação de matrícula p/ Reset;

    ## BOTÕES DA TOOLBAR ##
    tela_menu.home_btn.clicked.connect(user_marcaponto_pg)
    tela_menu.sair_btn.clicked.connect(sair)

    ## PAGINA DE DADOS ##
    tela_menu.meus_dados1_btn.clicked.connect(user_marcaponto_pg1)
    tela_menu.meus_dados2_btn.clicked.connect(user_marcaponto_pg1)
    tela_menu.data_edit_btn.clicked.connect(user_marcaponto_pg2)
    tela_menu.data_alterar_senha_btn.clicked.connect(user_marcaponto_pg3)
    #ui.data_salvar_btn1.clicked.connect(main_pg)
    #ui.data_salvar_btn2.clicked.connect(main_pg)

    ## PAGINA DE MARCA PONTO ##
    tela_menu.marcaponto_btn1.clicked.connect(user_marcaponto_pg4)
    tela_menu.marcaponto_btn2.clicked.connect(user_marcaponto_pg4)

    ## PAGINA DE RELATORIO ##
    tela_menu.relatorio_btn1.clicked.connect(user_marcaponto_pg5)
    tela_menu.relatorio_btn2.clicked.connect(user_marcaponto_pg5)

    tela_resete_confirma.busca_email_btn.clicked.connect(lambda: Win.recupera_senha(Win.tela_resete_confirma.user_email_edt.text()))
    tela_resete_altera.altera_senha_btn.clicked.connect(altera_cadastro)

    tela_cadastro.cadastra_func_btn.clicked.connect(cadastrar)  # Chama Funcao para cadastrar Colaborador;

    #tela_menu.DEFINIR_NOME_BOTÃO.clicked.connect(telaPonto)     # Chama tela de Ponto;
    #tela_menu_adm.DEFNIR_NOME_BOTÃO.clicked.connect(telaPonto)  # Chama tela de Ponto;

    tela_login.show()
    ######################################################################################

    #   tela_cadastro = uic.loadUi("tela_cadastro.ui")
    #   tela_login = uic.loadUi("tela_login.ui")
    #   tela_menu = uic.loadUi("tela_menu.ui")
    #   tela_menu_adm = uic.loadUi("tela_adm.ui")  - ##             Tela ainda não foi desenhada;
    #   tela_resete_confirma = uic.loadUi("tela_reset_confirm.ui")
    #   tela_resete_altera = uic.loadUi("tela_reset_altera.ui")



## variaveis:
user_email = ''
matricula = ''
Win.app.exec()

#if __name__ == '__main__':
    #app = Win.app
    #main_win = Win.MainWindow()
    #main_win.show()
    #sys.exit(app.exec_(Win.MainWindow()))