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
#from ui_tela_menu import Ui_MainWindow
#from ui_tela_menu import Ui_MainWindow_ADM



################################################################
## RECURSO PARA CRIPTOGRAFIA | THREADING | TIME
################################################################
from PyQt5.QtCore import pyqtSignal, QObject
import hashlib
import threading
import time
import datetime
import sys, os
import requests
from requests.structures import CaseInsensitiveDict


################################################################
## RECURSO INTERNOS CRIADOS PELOS ALUNOS
################################################################
import pega_horarioGP, geolocGP, gerarRelatorioGP
import ui_tela_menu
import ui_tela_adm


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

    def attDataAdm(self):
        Win.tela_menu_adm.lbl_data.setText(pega_horarioGP.curlSomenteHoraStr())

    def relogio(self):
        self.updateDate.connect(self.attData)
        while(True):
            time.sleep(1)
            if Win.tela_menu.stackedWidget.currentIndex() != 4:
                return
            self.updateDate.emit()

    def relogioAdm(self):
        self.updateDate.connect(self.attDataAdm)
        while(True):
            time.sleep(1)
            if Win.tela_menu_adm.stackedWidget.currentIndex() != 4:
                return
            self.updateDate.emit()

class Win():
    app = QtWidgets.QApplication([])
    wk = Worker()

    tela_cadastro = uic.loadUi("tela_cadastro.ui")
    tela_login = uic.loadUi("tela_login.ui")
    tela_menu = uic.loadUi("tela_menu.ui")
    tela_messageBox = uic.loadUi("tela_messageBox.ui")
    tela_menu_adm = uic.loadUi("tela_adm.ui")
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

            self.actionExit.triggered.connect(self.close)
          

    def messageBox(err):
            Win.tela_messageBox.txtMsg.setText(err)
            Win.tela_messageBox.show()

    def marcaPonto():
        data = pega_horarioGP.curlDiaStr()
        data_unix = pega_horarioGP.curlDiaUnix()
        hora = pega_horarioGP.curlSomenteHoraStr()
        utc = pega_horarioGP.verificarUTC(geolocGP.region())
        user_email = Win.tela_menu.lbl_email.text()
        justificativa = "OK"

        banco = sqlite3.connect('banco_cadastroGP.db') 
        cursor = banco.cursor()  
        cursor.execute("SELECT primeiro_nome FROM banco_cadastroGP WHERE user_email ='{}'".format(user_email))
        primeiro_nome = cursor.fetchone()
        cursor.execute("SELECT segundo_nome FROM banco_cadastroGP WHERE user_email ='{}'".format(user_email))
        segundo_nome = cursor.fetchone()
        cursor.execute("SELECT matricula FROM banco_cadastroGP WHERE user_email ='{}'".format(user_email))
        matricula = cursor.fetchone()
        banco.close()


        #Verifica número excessivo de pontos
        try:
            banco = sqlite3.connect('banco_pontoGP.db')
            cursor = banco.cursor()
            cursor.execute("SELECT hora FROM banco_pontoGP WHERE data = '"+data+"' AND matricula = '"+matricula[0]+"' ORDER BY data ASC")
        except sqlite3.Error as erro:
            Win.messageBox("Erro ao pesquisar os dados: "+str(erro))
            return
        pontos = cursor.fetchall()
        qtde_pontos = len(pontos)

        if qtde_pontos < 1: entrada = "Entrada"
        if qtde_pontos == 1: entrada = "Saída almoço"
        if qtde_pontos == 2: entrada = "Retorno almoço"
        if qtde_pontos == 3: entrada = "Saída"

        if qtde_pontos > 3:
            Win.messageBox("Número excessivo de pontos.")
            return

        try:
            banco = sqlite3.connect('banco_pontoGP.db') 
            cursor = banco.cursor()            
            cursor.execute("CREATE TABLE IF NOT EXISTS banco_pontoGP (primeiro_nome text,segundo_nome text,matricula text,data text,hora text,utc text,data_unix text,entrada text,justificativa text)")
            cursor.execute("INSERT INTO banco_pontoGP VALUES ('"+primeiro_nome[0]+"','"+segundo_nome[0]+"','"+matricula[0]+"','"+data+"','"+hora+"','"+utc+"','"+str(data_unix)+"','"+entrada+"','"+justificativa+"')")
            banco.commit() 
            banco.close()
            Win.messageBox("Ponto registrado com sucesso.")

        except sqlite3.Error as erro:
            Win.messageBox("Erro ao inserir os dados: "+str(erro))
            return
    
    def marcaPontoADM():
        data = pega_horarioGP.curlDiaStr()
        data_unix = pega_horarioGP.curlDiaUnix()
        hora = pega_horarioGP.curlSomenteHoraStr()
        utc = pega_horarioGP.verificarUTC(geolocGP.region())
        user_email = Win.tela_menu_adm.lbl_email.text()
        justificativa = "OK"

        banco = sqlite3.connect('banco_cadastroGP.db') 
        cursor = banco.cursor()  
        cursor.execute("SELECT primeiro_nome FROM banco_cadastroGP WHERE user_email ='{}'".format(user_email))
        primeiro_nome = cursor.fetchone()
        cursor.execute("SELECT segundo_nome FROM banco_cadastroGP WHERE user_email ='{}'".format(user_email))
        segundo_nome = cursor.fetchone()
        cursor.execute("SELECT matricula FROM banco_cadastroGP WHERE user_email ='{}'".format(user_email))
        matricula = cursor.fetchone()

        #Verifica número excessivo de pontos
        try:
            banco = sqlite3.connect('banco_pontoGP.db') 
            cursor = banco.cursor()
            cursor.execute("SELECT hora FROM banco_pontoGP WHERE data = '"+data+"' AND matricula = '"+matricula[0]+"' ORDER BY data ASC")
        except sqlite3.Error as erro:
            Win.messageBox("Erro ao pesquisar os dados: "+str(erro))
            return
        pontos = cursor.fetchall()
        qtde_pontos = len(pontos)


        if qtde_pontos < 1: entrada = "Entrada"
        if qtde_pontos == 1: entrada = "Saída p/ Almoço"
        if qtde_pontos == 2: entrada = "Retorno d/ Almoço"
        if qtde_pontos == 3: entrada = "Saída"

        if qtde_pontos > 3:
            Win.messageBox("Número excessivo de pontos.")
            return


        try:
            banco = sqlite3.connect('banco_pontoGP.db') 
            cursor = banco.cursor()            
            cursor.execute("CREATE TABLE IF NOT EXISTS banco_pontoGP (primeiro_nome text,segundo_nome text,matricula text,data text,hora text,utc text,data_unix text,entrada text,justificativa text)")
            cursor.execute("INSERT INTO banco_pontoGP VALUES ('"+primeiro_nome[0]+"','"+segundo_nome[0]+"','"+matricula[0]+"','"+data+"','"+hora+"','"+utc+"','"+str(data_unix)+"','"+entrada+"','"+justificativa+"')")
            banco.commit() 
            banco.close()
            Win.messageBox("Ponto registrado com sucesso.")

        except sqlite3.Error as erro:
            Win.messageBox("Erro ao inserir os dados: "+str(erro))
            return
    
    def gerarRelatorio():
        #Gera data inicial em formato unix
        try:
            data_inicial_str = [
                int(Win.tela_menu.inicial_aaaa_edt.text())\
                ,int(Win.tela_menu.inicial_mm_edt.text())\
                ,int(Win.tela_menu.inicial_dd_edt.text())]
            
            data_final_str = [
                int(Win.tela_menu.final_aaaa_edt.text())\
                ,int(Win.tela_menu.final_mm_edt.text())\
                ,int(Win.tela_menu.final_dd_edt.text())]

            #Gera data inicial em formato unix
            data_inicial = datetime.date(data_inicial_str[0], data_inicial_str[1], data_inicial_str[2])
            data_inicial_unix = time.mktime(data_inicial.timetuple())

            #Gera data final em formato unix
            data_final = datetime.datetime(data_final_str[0], data_final_str[1], data_final_str[2], 23, 59, 59)
            data_final_unix = time.mktime(data_final.timetuple())
        except:
            Win.messageBox("Data inválida.")
            return
        
        mesma_data = False
        if data_inicial_str == data_final_str:
            mesma_data = True

        gerarRelatorioGP.gerarArquivo(Win.tela_menu.username_txt_2.text()[6:],
        Win.tela_menu.matricula_txt_2.text()[11:],
        str(data_inicial_unix)[:-2],
        str(data_final_unix)[:-2],
        mesma_data)

        Win.messageBox("Relatório gerado com sucesso.")
        return

    def gerarRelatorioAdm():
        try:
            data_inicial_adm_str = [
                int(Win.tela_menu_adm.inicial_aaaa_edt.text())\
                ,int(Win.tela_menu_adm.inicial_mm_edt.text())\
                ,int(Win.tela_menu_adm.inicial_dd_edt.text())]
            
            data_final_adm_str = [
                int(Win.tela_menu_adm.final_aaaa_edt.text())\
                ,int(Win.tela_menu_adm.final_mm_edt.text())\
                ,int(Win.tela_menu_adm.final_dd_edt.text())]

            #Gera data inicial em formato unix - ADM
            data_inicial_adm = datetime.date(data_inicial_adm_str[0], data_inicial_adm_str[1], data_inicial_adm_str[2])
            data_inicial_unix_adm = time.mktime(data_inicial_adm.timetuple())

            #Gera data final em formato unix - ADM
            data_final_adm = datetime.datetime(data_final_adm_str[0], data_final_adm_str[1], data_final_adm_str[2], 23, 59, 59)
            data_final_unix_adm = time.mktime(data_final_adm.timetuple())
        except:
            Win.messageBox("Data inválida.")
            return
        
        mesma_data = False
        if data_inicial_adm_str == data_final_adm_str:
            mesma_data = True

        gerarRelatorioGP.gerarArquivo(Win.tela_menu_adm.username_txt_2.text()[6:],
        Win.tela_menu_adm.matricula_txt_2.text()[11:],
        str(data_inicial_unix_adm)[:-2],
        str(data_final_unix_adm)[:-2],
        mesma_data)

        Win.messageBox("Relatório gerado com sucesso.")
        return
    
    
    def gerarRelatorioDia():
        gerarRelatorioGP.gerarArquivoDia(Win.tela_menu_adm.username_txt_2.text()[6:],
        Win.tela_menu.matricula_txt_2.text()[11:])

        Win.messageBox("Relatório gerado com sucesso.")
        return
    
    def gerarRelatorioSemana():
        gerarRelatorioGP.gerarArquivoSemana(Win.tela_menu_adm.username_txt_2.text()[6:],
        Win.tela_menu.matricula_txt_2.text()[11:])

        Win.messageBox("Relatório gerado com sucesso.")
        return
    

    def gerarRelatorioMes():
        gerarRelatorioGP.gerarArquivoMes(Win.tela_menu_adm.username_txt_2.text()[6:],
        Win.tela_menu.matricula_txt_2.text()[11:])

        Win.messageBox("Relatório gerado com sucesso.")
        return
    
    def gerarRelatorioDiaADM():
        gerarRelatorioGP.gerarArquivoDia(Win.tela_menu_adm.username_txt_2.text()[6:],
        Win.tela_menu_adm.matricula_txt_2.text()[11:])

        Win.messageBox("Relatório gerado com sucesso.")
        return
    
    def gerarRelatorioSemanaADM():
        gerarRelatorioGP.gerarArquivoSemana(Win.tela_menu_adm.username_txt_2.text()[6:],
        Win.tela_menu_adm.matricula_txt_2.text()[11:])

        Win.messageBox("Relatório gerado com sucesso.")
        return
    

    def gerarRelatorioMesADM():
        gerarRelatorioGP.gerarArquivoMes(Win.tela_menu_adm.username_txt_2.text()[6:],
        Win.tela_menu_adm.matricula_txt_2.text()[11:])

        Win.messageBox("Relatório gerado com sucesso.")
        return


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
            cursor.execute("SELECT senha FROM banco_cadastroGP WHERE user_email ='{}'".format(user_email))
            senha_bd = cursor.fetchone()
            cursor.execute("SELECT admin FROM banco_cadastroGP WHERE user_email = '{}'".format(user_email))
            admVR = cursor.fetchone()
            cursor.execute("SELECT primeiro_nome, segundo_nome, cargo, matricula, user_email FROM banco_cadastroGP WHERE user_email ='{}'".format(user_email))
            content_bd = cursor.fetchone()
            banco.close()


            if hashlib.sha256(senha.encode('utf-8')).hexdigest() == senha_bd[0]:
                if admVR[0] == 1: 
                    try:
                        Win.tela_login.close()
                        Win.tela_menu_adm.show()
                        Win.tela_menu_adm.lbl_nome.setText(content_bd[0]+" "+content_bd[1])
                        Win.tela_menu_adm.lbl_cargo.setText(content_bd[2])
                        Win.tela_menu_adm.lbl_matricula.setText(content_bd[3])
                        Win.tela_menu_adm.lbl_email.setText(content_bd[4])

                        Win.tela_menu_adm.username_txt.setText("Nome: "+content_bd[0]+" "+content_bd[1])
                        Win.tela_menu_adm.cargo_txt.setText("Cargo: "+content_bd[2])
                        Win.tela_menu_adm.matricula_txt.setText("Matrícula: "+content_bd[3])

                        Win.tela_menu_adm.username_txt_2.setText("Nome: "+content_bd[0]+" "+content_bd[1])
                        Win.tela_menu_adm.cargo_txt_2.setText("Cargo: "+content_bd[2])
                        Win.tela_menu_adm.matricula_txt_2.setText("Matrícula: "+content_bd[3])
                    except ValueError as err:
                        Win.messageBox(err)         
                else: 
                    try:
                        Win.tela_login.close()                        
                        Win.tela_menu.show()
                        Win.tela_menu.lbl_nome.setText(content_bd[0]+" "+content_bd[1])
                        Win.tela_menu.lbl_cargo.setText(content_bd[2])
                        Win.tela_menu.lbl_matricula.setText(content_bd[3])
                        Win.tela_menu.lbl_email.setText(content_bd[4])

                        Win.tela_menu.username_txt.setText("Nome: "+content_bd[0]+" "+content_bd[1])
                        Win.tela_menu.cargo_txt.setText("Cargo: "+content_bd[2])
                        Win.tela_menu.matricula_txt.setText("Matrícula: "+content_bd[3])

                        Win.tela_menu.username_txt_2.setText("Nome: "+content_bd[0]+" "+content_bd[1])
                        Win.tela_menu.cargo_txt_2.setText("Cargo: "+content_bd[2])
                        Win.tela_menu.matricula_txt_2.setText("Matrícula: "+content_bd[3])
                    except ValueError as err:
                        Win.messageBox(err)
                        
            else:
                Win.messageBox("Dados de login incorretos!")
                Win.tela_login.user_login_edt.setText('')
                Win.tela_login.user_password_edt.setText('')
        except:
            Win.messageBox("Erro ao validar o Login")

    ##################################
    # Telas | CADASTRO
    ##################################
    def chama_cad():
        Win.tela_cadastro.show()
    
    def fecha_Cad():
        Win.tela_cadastro.close()
        Win.tela_login.show()

    def cadastrar():
        primeiro_nome = Win.tela_cadastro.primeiro_nome_edt.text()
        segundo_nome = Win.tela_cadastro.segundo_nome_edt.text()
        user_email = Win.tela_cadastro.user_email_edt.text()
        senha = hashlib.sha256(Win.tela_cadastro.user_password_edt.text().encode('utf-8')).hexdigest()
        c_senha = hashlib.sha256(Win.tela_cadastro.user_password2_edt.text().encode('utf-8')).hexdigest()
        admin = 0
        matricula = "n/a"
        cargo = "n/a"

        def telaCadastroLimpa():
            Win.tela_cadastro.primeiro_nome_edt.setText('')
            Win.tela_cadastro.segundo_nome_edt.setText('')
            Win.tela_cadastro.user_email_edt.setText('')
            Win.tela_cadastro.user_password_edt.setText('')
            Win.tela_cadastro.user_password2_edt.setText('')

        if (senha == c_senha):
            try:
                banco = sqlite3.connect('banco_cadastroGP.db') 
                cursor = banco.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS banco_cadastroGP (primeiro_nome text,segundo_nome text,user_email text,senha text, admin integer,cargo text,matricula text)")
                cursor.execute("SELECT matricula FROM banco_cadastroGP ORDER BY matricula DESC")

                matricula_str = int(cursor.fetchone()[0])+1
                matricula = str(matricula_str).rjust(4, '0')

                cursor.execute("INSERT INTO banco_cadastroGP VALUES ('"+primeiro_nome+"','"+segundo_nome+"','"+user_email+"','"+senha+"','"+str(admin)+"','"+cargo+"','"+matricula+"')")

                banco.commit() 
                banco.close()
                Win.messageBox("Usuario cadastrado com sucesso")

            except sqlite3.Error as erro:
                Win.messageBox("Erro ao inserir os dados: "+str(erro))
            Win.tela_cadastro.close()
            telaCadastroLimpa()
            Win.tela_login.show()


        else:
            Win.messageBox("As senhas digitadas estão diferentes")
            Win.tela_cadastro.user_password_edt.setText('')
            Win.tela_cadastro.user_password2_edt.setText('')
    
    ##################################
    # Telas | RESET CONFIRM - CONSTRUINDO (NÃO LINKADO)
    ##################################     

    def reset_confirm():
        Win.tela_resete_confirma.show()
        

    def recupera_senha(user_email):
        banco = sqlite3.connect('banco_cadastroGP.db') 
        cursor = banco.cursor()
        cursor.execute("SELECT user_email FROM banco_cadastroGP WHERE user_email = '{}'".format(user_email))
        user_emailVR = cursor.fetchone()
        banco.close()
        if not user_emailVR:
            Win.messageBox("Usuário não encontrado")
            Win.tela_resete_confirma.close()
            Win.tela_login.show()
            return
        
        if user_email == user_emailVR[0]:
            
            #Gera o token a partir de um request HTTP e configura os headers e dados

            url = "http://192.168.1.18:8080/getMfaCode"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/json"

            data = '{"email":"'+user_email+'", "usrToken":"", "operacao":"1"}'

            resposta = requests.post(url, headers=headers, data=data).text

            if resposta != "True":
                Win.messageBox("Erro ao gerar token.")

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
        codigo = Win.tela_resete_altera.codigo_edt.text()       # Função não está sendo usada
        senha = hashlib.sha256(Win.tela_resete_altera.user_password_edt.text().encode('utf-8')).hexdigest()
        c_senha = hashlib.sha256(Win.tela_resete_altera.user_password2_edt.text().encode('utf-8')).hexdigest()

        #checka o token
        url = "http://192.168.1.18:8080/getMfaCode"

        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"

        data = '{"email":"'+user_email+'", "usrToken":"'+codigo+'", "operacao":"0"}'

        resposta = requests.post(url, headers=headers, data=data).text

        if(resposta != "True"):
            Win.messageBox("Token inválido.")
            return
        
        if (senha == c_senha):
            try:
                banco = sqlite3.connect('banco_cadastroGP.db') 
                cursor = banco.cursor()
                cursor.execute("UPDATE banco_cadastroGP SET senha = '"+senha+"' WHERE user_email = '{}'".format(user_email))
                banco.commit() 
                banco.close()
                Win.messageBox("Usuario atualizado com sucesso")

            except sqlite3.Error as erro:
                Win.messageBox("Erro ao inserir os dados: "+str(erro))
            Win.tela_resete_altera.codigo_edt.setText('')
            Win.tela_resete_altera.user_password_edt.setText('')
            Win.tela_resete_altera.user_password2_edt.setText('')
            Win.tela_resete_altera.close()
            Win.tela_login.show()

        else:
            Win.messageBox("As senhas digitadas estão diferentes")
            Win.tela_resete_altera.user_password_edt.setText('')
            Win.tela_resete_altera.user_password2_edt.setText('')
    
    ##################################
    # Telas | MENU - CONSTRUINDO
    ##################################

    def user_main_pg():
        Win.tela_menu.stackedWidget.setCurrentIndex(0)

    def user_data_view():
        Win.tela_menu.stackedWidget.setCurrentIndex(1)

    def user_data_change_pg1():
        Win.tela_menu.stackedWidget.setCurrentIndex(2)

    def user_data_change_pg2():
        Win.tela_menu.stackedWidget.setCurrentIndex(3)

    def user_marcaponto_pg4():
        #Coletor de variaveis
        coletor = []

        Win.tela_menu.stackedWidget.setCurrentIndex(4)

        Win.tela_menu.lbl_dia.setText(pega_horarioGP.curlDiaSemanaStr()+", "+pega_horarioGP.curlDiaStr())
        Win.tela_menu.lbl_data.setText(pega_horarioGP.curlSomenteHoraStr())

        matricula = Win.tela_menu.matricula_txt.text()[11:]+""
        data = pega_horarioGP.curlDiaStr()

        banco = sqlite3.connect('banco_pontoGP.db') 
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT hora FROM banco_pontoGP WHERE data = '"+data+"' AND matricula = '"+matricula+"' ORDER BY data ASC")
        except sqlite3.Error as erro:
                Win.messageBox("Erro ao pesquisar os dados: "+str(erro))

        pontos = cursor.fetchall()
        banco.close()

        qtde_pontos = len(pontos)

        if qtde_pontos < 1: None
        if qtde_pontos >= 1:    Win.tela_menu.lbl_entrada.setText("Ponto de entrada\n" + pontos[0][0])
        if qtde_pontos > 1: Win.tela_menu.lbl_intervalo_inicio.setText("Saída p/ almoço:\n" + pontos[1][0])
        if qtde_pontos > 2: Win.tela_menu.lbl_intervalo_retorno.setText("Retorno do almoço:\n" + pontos[2][0])
        if qtde_pontos > 3: Win.tela_menu.lbl_saida.setText("Ponto de saída\n" + pontos[3][0])
        if qtde_pontos > 4: Win.messageBox("Irregularidades no ponto de hoje, falar com o administrador")

        coletor.append("matricula")
        coletor.append("data")
        coletor.append("banco")
        coletor.append("cursor")
        coletor.append("pontos")
        coletor.append("qtde_pontos")

        for var in coletor:
            del var

        threading.Thread(target=Win.wk.relogio).start()

    def relatorio_fr_pg():
        Win.tela_menu.stackedWidget.setCurrentIndex(5)

    ##################################
    # Telas | MENU ADM - CONSTRUINDO
    ##################################

    def user_main_pg_adm():
        Win.tela_menu_adm.stackedWidget.setCurrentIndex(0)

    def user_data_view_adm():
        Win.tela_menu_adm.stackedWidget.setCurrentIndex(1)

    def user_data_change_pg1_adm():
        Win.tela_menu_adm.stackedWidget.setCurrentIndex(2)

    def user_data_change_pg2_adm():
        Win.tela_menu_adm.stackedWidget.setCurrentIndex(3)

    def user_marcaponto_pg4_adm():
        #Coletor de variaveis
        coletor = []

        Win.tela_menu_adm.stackedWidget.setCurrentIndex(4)

        Win.tela_menu_adm.lbl_dia.setText(pega_horarioGP.curlDiaSemanaStr()+", "+pega_horarioGP.curlDiaStr())
        Win.tela_menu_adm.lbl_data.setText(pega_horarioGP.curlSomenteHoraStr())

        matricula_adm = Win.tela_menu_adm.matricula_txt.text()[11:]+""
        data = pega_horarioGP.curlDiaStr()

        banco = sqlite3.connect('banco_pontoGP.db') 
        cursor_adm = banco.cursor()
        try:
            cursor_adm.execute("SELECT hora FROM banco_pontoGP WHERE data = '"+data+"' AND matricula = '"+matricula_adm+"' ORDER BY data ASC")
        except sqlite3.Error as erro:
                Win.messageBox("Erro ao pesquisar os dados: "+str(erro))
        pontos_adm = cursor_adm.fetchall()
        banco.close()
        qtde_pontos_adm = len(pontos_adm)

        if qtde_pontos_adm < 1: None
        if qtde_pontos_adm >= 1:    Win.tela_menu_adm.lbl_entrada.setText("Ponto de entrada\n" + pontos_adm[0][0])
        if qtde_pontos_adm > 1: Win.tela_menu_adm.lbl_intervalo_inicio.setText("Saída p/ almoço:\n" + pontos_adm[1][0])
        if qtde_pontos_adm > 2: Win.tela_menu_adm.lbl_intervalo_retorno.setText("Retorno do almoço:\n" + pontos_adm[2][0])
        if qtde_pontos_adm > 3: Win.tela_menu_adm.lbl_saida.setText("Ponto de saída\n" + pontos_adm[3][0])
        if qtde_pontos_adm > 4: Win.messageBox("Irregularidades no ponto de hoje, falar com o administrador")

        coletor.append("matricula_adm")
        coletor.append("data")
        coletor.append("banco")
        coletor.append("cursor_adm")
        coletor.append("pontos_adm")
        coletor.append("qtde_pontos_adm")

        for var in coletor:
            del var

        threading.Thread(target=Win.wk.relogioAdm).start()

    def relatorio_fr_pg_adm():
        Win.tela_menu_adm.stackedWidget.setCurrentIndex(5)
    
    def funcionarios_cad_pg_adm():
        Win.tela_menu_adm.stackedWidget.setCurrentIndex(6)

    ##################################
    # FIM Telas | MENU ADM - CONSTRUINDO
    ##################################
    
    def sair():
        os._exit(1)
 
    def complementa_cad_defineADM():
        user_email = Win.tela_menu_adm.email_funcionario_edt.text()
        cargo = Win.tela_menu_adm.cargo_edt.text()
        matricula = Win.tela_menu_adm.matricula_edt.text()
        admin = ''

        if Win.tela_menu_adm.confirm_sim.isChecked():
            admin = 1
            try:
                banco = sqlite3.connect('banco_cadastroGP.db') 
                cursor = banco.cursor()
                cursor.execute("UPDATE banco_cadastroGP SET admin = '"+str(admin)+"' WHERE user_email = '{}'".format(user_email))
                cursor.execute("UPDATE banco_cadastroGP SET cargo = '"+cargo+"' WHERE user_email = '{}'".format(user_email))
                cursor.execute("UPDATE banco_cadastroGP SET matricula = '"+matricula+"' WHERE user_email = '{}'".format(user_email))
                banco.commit() 
                banco.close()
                Win.messageBox("Usuario atualizado com sucesso")

            except sqlite3.Error as erro:
                Win.messageBox("Erro ao inserir os dados: "+str(erro))
        if Win.tela_menu_adm.confirm_nao.isChecked():
            admin = 0
            try:
                banco = sqlite3.connect('banco_cadastroGP.db') 
                cursor = banco.cursor()
                cursor.execute("UPDATE banco_cadastroGP SET admin = '"+str(admin)+"' WHERE user_email = '{}'".format(user_email))
                cursor.execute("UPDATE banco_cadastroGP SET cargo = '"+cargo+"' WHERE user_email = '{}'".format(user_email))
                cursor.execute("UPDATE banco_cadastroGP SET matricula = '"+matricula+"' WHERE user_email = '{}'".format(user_email))
                banco.commit() 
                banco.close()
                Win.messageBox("Usuario atualizado com sucesso")

            except sqlite3.Error as erro:
                Win.messageBox("Erro ao inserir os dados: "+str(erro))
    
    def atualizada_cad_logado():            #ATUALIZA PRIMEIRO E SEGUNDO NOME, E-MAIL;
        user_email = Win.tela_menu.email_edt.text()
        primeiro_nome = Win.tela_menu.primeiro_nome_edt.text()
        segundo_nome = Win.tela_menu.segundo_nome_edt.text()


        try:
            banco = sqlite3.connect('banco_cadastroGP.db') 
            cursor = banco.cursor()
            cursor.execute("UPDATE banco_cadastroGP SET primeiro_nome = '"+primeiro_nome+"' WHERE user_email = '{}'".format(user_email))
            cursor.execute("UPDATE banco_cadastroGP SET segundo_nome = '"+segundo_nome+"' WHERE user_email = '{}'".format(user_email))
            cursor.execute("UPDATE banco_cadastroGP SET user_email = '"+user_email+"' WHERE user_email = '{}'".format(user_email))
            banco.commit() 
            banco.close()
            Win.messageBox("Usuario atualizado com sucesso")
            Win.tela_menu.email_edt.setText('')
            Win.tela_menu.primeiro_nome_edt.setText('')
            Win.tela_menu.segundo_nome_edt.setText('')

        except sqlite3.Error as erro:
            Win.messageBox("Erro ao inserir os dados: "+str(erro))
              
    def atualizada_cad_logado2():           #ATUALIZA PRIMEIRO E SEGUNDO NOME, E-MAIL - SENHA;
        Win.tela_menu.email_edt.setText('')
        Win.tela_menu.primeiro_nome_edt.setText('')
        Win.tela_menu.segundo_nome_edt.setText('')

        user_email = Win.tela_menu.email_edt2.text()
        primeiro_nome = Win.tela_menu.primeiro_nome_edt2.text()
        segundo_nome = Win.tela_menu.segundo_nome_edt2.text()

        senha_atual = hashlib.sha256(Win.tela_menu.senha_atual_edt.text().encode('utf-8')).hexdigest()
        nova_senha = hashlib.sha256(Win.tela_menu.senha_nova_edt.text().encode('utf-8')).hexdigest()
        c_nova_senha = hashlib.sha256(Win.tela_menu.senha_nova_confirma_edt.text().encode('utf-8')).hexdigest()

        def telaMenuLimpa():
            Win.tela_menu.email_edt2.setText('')
            Win.tela_menu.primeiro_nome_edt2.setText('')
            Win.tela_menu.segundo_nome_edt2.setText('')
            Win.tela_menu.senha_atual_edt.setText('')
            Win.tela_menu.senha_nova_edt.setText('')
            Win.tela_menu.senha_nova_confirma_edt.setText('')

        if Win.tela_menu.confirm_alterar.isChecked():
            banco = sqlite3.connect('banco_cadastroGP.db') 
            cursor = banco.cursor()
            cursor.execute("SELECT senha FROM banco_cadastroGP WHERE user_email ='{}'".format(user_email))
            senha_bd = cursor.fetchone()

            if senha_atual == senha_bd[0]:
                try:
                    if (nova_senha == c_nova_senha):
                        cursor.execute("UPDATE banco_cadastroGP SET primeiro_nome = '"+primeiro_nome+"' WHERE user_email = '{}'".format(user_email))
                        cursor.execute("UPDATE banco_cadastroGP SET segundo_nome = '"+segundo_nome+"' WHERE user_email = '{}'".format(user_email))
                        cursor.execute("UPDATE banco_cadastroGP SET user_email = '"+user_email+"' WHERE user_email = '{}'".format(user_email))
                        cursor.execute("UPDATE banco_cadastroGP SET senha = '"+nova_senha+"' WHERE user_email = '{}'".format(user_email))
                        banco.commit() 
                        banco.close()

                        Win.messageBox("Usuario atualizado com sucesso")
                        telaMenuLimpa()

                    else:
                        Win.messageBox("As senhas digitadas estão diferentes")
                        telaMenuLimpa()

                except sqlite3.Error as erro:
                    Win.messageBox("Erro ao inserir os dados: "+str(erro))

        if Win.tela_menu.confirm_cancelar.isChecked():
            Win.messageBox("Não foram efetuadas mudanças no seu perfil")
            telaMenuLimpa()

    def atualizada_cad_logado_ADM():            #ATUALIZA PRIMEIRO E SEGUNDO NOME, E-MAIL;
        user_email = Win.tela_menu_adm.email_edt.text()
        primeiro_nome = Win.tela_menu_adm.primeiro_nome_edt.text()
        segundo_nome = Win.tela_menu_adm.segundo_nome_edt.text()

        try:
            banco = sqlite3.connect('banco_cadastroGP.db') 
            cursor = banco.cursor()
            cursor.execute("UPDATE banco_cadastroGP SET primeiro_nome = '"+primeiro_nome+"' WHERE user_email = '{}'".format(user_email))
            cursor.execute("UPDATE banco_cadastroGP SET segundo_nome = '"+segundo_nome+"' WHERE user_email = '{}'".format(user_email))
            cursor.execute("UPDATE banco_cadastroGP SET user_email = '"+user_email+"' WHERE user_email = '{}'".format(user_email))
            banco.commit() 
            banco.close()
            Win.messageBox("Usuario atualizado com sucesso")
            Win.tela_menu_adm.email_edt.setText('')
            Win.tela_menu_adm.primeiro_nome_edt.setText('')
            Win.tela_menu_adm.segundo_nome_edt.setText('')

        except sqlite3.Error as erro:
            Win.messageBox("Erro ao inserir os dados: "+str(erro))
              
    def atualizada_cad_logado2_ADM():           #ATUALIZA PRIMEIRO E SEGUNDO NOME, E-MAIL - SENHA;
        Win.tela_menu_adm.email_edt.setText('')
        Win.tela_menu_adm.primeiro_nome_edt.setText('')
        Win.tela_menu_adm.segundo_nome_edt.setText('')

        user_email = Win.tela_menu_adm.email_edt2.text()
        primeiro_nome = Win.tela_menu_adm.primeiro_nome_edt2.text()
        segundo_nome = Win.tela_menu_adm.segundo_nome_edt2.text()

        senha_atual = hashlib.sha256(Win.tela_menu_adm.senha_atual_edt.text().encode('utf-8')).hexdigest()
        nova_senha = hashlib.sha256(Win.tela_menu_adm.senha_nova_edt.text().encode('utf-8')).hexdigest()
        c_nova_senha = hashlib.sha256(Win.tela_menu_adm.senha_nova_confirma_edt.text().encode('utf-8')).hexdigest()

        def telaMenuAdmLimpa():        
            Win.tela_menu_adm.email_edt2.setText('')
            Win.tela_menu_adm.primeiro_nome_edt2.setText('')
            Win.tela_menu_adm.segundo_nome_edt2.setText('')
            Win.tela_menu_adm.senha_atual_edt.setText('')
            Win.tela_menu_adm.senha_nova_edt.setText('')
            Win.tela_menu_adm.senha_nova_confirma_edt.setText('')

        if Win.tela_menu_adm.confirm_alterar.isChecked():
            banco = sqlite3.connect('banco_cadastroGP.db') 
            cursor = banco.cursor()
            cursor.execute("SELECT senha FROM banco_cadastroGP WHERE user_email ='{}'".format(user_email))
            senha_bd = cursor.fetchone()

            if senha_atual == senha_bd[0]:
                try:
                    if (nova_senha == c_nova_senha):
                        cursor.execute("UPDATE banco_cadastroGP SET primeiro_nome = '"+primeiro_nome+"' WHERE user_email = '{}'".format(user_email))
                        cursor.execute("UPDATE banco_cadastroGP SET segundo_nome = '"+segundo_nome+"' WHERE user_email = '{}'".format(user_email))
                        cursor.execute("UPDATE banco_cadastroGP SET user_email = '"+user_email+"' WHERE user_email = '{}'".format(user_email))
                        cursor.execute("UPDATE banco_cadastroGP SET senha = '"+nova_senha+"' WHERE user_email = '{}'".format(user_email))
                        banco.commit() 
                        banco.close()

                        Win.messageBox("Usuario atualizado com sucesso")
                        telaMenuAdmLimpa()

                    else:
                        Win.messageBox("As senhas digitadas estão diferentes")
                        telaMenuAdmLimpa()

                except sqlite3.Error as erro:
                    Win.messageBox("Erro ao inserir os dados: "+str(erro))

        if Win.tela_menu_adm.confirm_cancelar.isChecked():
            Win.messageBox("Não foram efetuadas mudanças no seu perfil")
            telaMenuAdmLimpa()

    #############################################################################################################################
    ##                                                LÓGICA DE BOTÕES                                                         ##
    #############################################################################################################################
    
    tela_login.login_btn.clicked.connect(login)                                      # Chama Função que verifica Login;
    tela_login.cadastra_btn.clicked.connect(chama_cad)                               # Chama tela de Cadastro;
    tela_login.user_password_edt.setEchoMode(QtWidgets.QLineEdit.Password)           # ;
    tela_login.recupera_btn.clicked.connect(reset_confirm)                           # Chama confirmação de matrícula p/ Reset;
    tela_login.first_acess_btn.clicked.connect(chama_cad)

    ## BOTÕES DA TOOLBAR ##
    tela_menu.home_btn.clicked.connect(user_main_pg)
    tela_menu.sair_btn.clicked.connect(sair)
    tela_menu.meus_dados1_btn.clicked.connect(user_data_view)
    tela_menu.marcaponto_btn1.clicked.connect(user_marcaponto_pg4)
    tela_menu.relatorio_btn1.clicked.connect(relatorio_fr_pg)

    tela_menu_adm.home_btn.clicked.connect(user_main_pg_adm)
    tela_menu_adm.sair_btn.clicked.connect(sair)
    tela_menu_adm.meus_dados1_btn.clicked.connect(user_data_view_adm)
    tela_menu_adm.marcaponto_btn1.clicked.connect(user_marcaponto_pg4_adm)
    tela_menu_adm.relatorio_btn1.clicked.connect(relatorio_fr_pg_adm)
    tela_menu_adm.funcionarios_btn.clicked.connect(funcionarios_cad_pg_adm)


    ## PAGINA DE DADOS ##
    tela_menu.meus_dados2_btn.clicked.connect(user_data_view)
    tela_menu.data_edit_btn.clicked.connect(user_data_change_pg1)
    tela_menu.data_alterar_senha_btn.clicked.connect(user_data_change_pg2)

    tela_menu_adm.meus_dados2_btn.clicked.connect(user_data_view_adm)
    tela_menu_adm.data_edit_btn.clicked.connect(user_data_change_pg1_adm)
    tela_menu_adm.data_alterar_senha_btn.clicked.connect(user_data_change_pg2_adm)


    ## PAGINA DE MARCA PONTO ##

    tela_menu.marcaponto_btn2.clicked.connect(user_marcaponto_pg4)
    tela_menu_adm.marcaponto_btn2.clicked.connect(user_marcaponto_pg4_adm)

    ## PAGINA DE RELATORIO ##

    tela_menu.relatorio_btn2.clicked.connect(relatorio_fr_pg)
    tela_menu_adm.relatorio_btn2.clicked.connect(relatorio_fr_pg_adm)

    ## PAGINA DE FUNCIONÁRIOS (AMD) ##

    tela_menu_adm.funcionarios_btn2.clicked.connect(funcionarios_cad_pg_adm)

    ## TELA RESET ##

    tela_resete_confirma.busca_email_btn.clicked.connect(lambda: Win.recupera_senha(Win.tela_resete_confirma.user_email_edt.text()))
    tela_resete_altera.altera_senha_btn.clicked.connect(altera_cadastro)

    ## TELA CADASTRO ##

    tela_cadastro.cadastra_func_btn.clicked.connect(cadastrar)  # Chama Funcao para cadastrar Colaborador;
    tela_cadastro.back_button.clicked.connect(fecha_Cad)        # Fecha tela cadastro e retorna a tela login;

    ## TELA MARCA PONTO ##

    tela_menu.registra_ponto_btn.clicked.connect(marcaPonto)
    tela_menu_adm.registra_ponto_btn.clicked.connect(marcaPontoADM)

    ##PERFIL ATUALIZAR LOGADO ##


    tela_menu.data_salvar_btn1.clicked.connect(atualizada_cad_logado)
    tela_menu.data_salvar_btn2.clicked.connect(atualizada_cad_logado2)

    tela_menu_adm.data_salvar_btn1.clicked.connect(atualizada_cad_logado_ADM)
    tela_menu_adm.data_salvar_btn2.clicked.connect(atualizada_cad_logado2_ADM)

    ##FUNCIONÁRIOS ATUALIZAR - ADM##
    tela_menu_adm.funcionario_cad_btn.clicked.connect(complementa_cad_defineADM)

    ##TELA DE GERAR RELATÓRIO
    tela_menu.gera_fr_btn.clicked.connect(gerarRelatorio)
    tela_menu_adm.gera_fr_btn.clicked.connect(gerarRelatorioAdm)

    tela_menu.fr_dia_btn.clicked.connect(gerarRelatorioDia)
    tela_menu.fr_semana_btn.clicked.connect(gerarRelatorioSemana)
    tela_menu.fr_mes_btn.clicked.connect(gerarRelatorioMes)

    tela_menu_adm.fr_dia_btn.clicked.connect(gerarRelatorioDiaADM)
    tela_menu_adm.fr_semana_btn.clicked.connect(gerarRelatorioSemanaADM)
    tela_menu_adm.fr_mes_btn.clicked.connect(gerarRelatorioMesADM)

    ## CHAMADA PROGRAM - TELA 01 ##

    tela_login.show()
#############################################################################################################################
##                                                            VARIÁVEIS:                                                   ##
#############################################################################################################################
user_email = ''
matricula = ''
primeiro_nome = ''
segundo_nome = ''
Win.app.exec()