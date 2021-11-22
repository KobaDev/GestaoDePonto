################################################################
## IMPORT DE RECURSO PARA INTERAÇÃO COM HORA CERTA
################################################################
import requests
import datetime
import geolocGP

################################################################
## DEFININDO ESTADOS DO BRASIL, SIGLAS
################################################################
utc_5 = ['AC']
utc_4 = ['AM', 'MT', 'MS', 'RO', 'RR']
utc_3 = ['AL', 'AP', 'BA', 'CE', 'ES', 'GO', 'MA', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'SP', 'SC', 'SE', 'TO', 'DF']

################################################################
## VERIFICAÇÃO DE FUSO DA REGIÃO, APLICANDO + | - HORAS AO FUSO
################################################################
def verificarUTC_num(region):
    if region in utc_5:
        return -7200 #Retira 2 horas do horário de Brasília
    elif region in utc_4:
        return -3600 #Retira 1 hora do horário de Brasília
    elif region in utc_3:
        return 0     #Horário de Brasília
    else:
        return 3600

################################################################
## VERIFICA EM QUAL ESTADO O USUÁRIO ESTÁ, APLICANDO O UTC
################################################################
def verificarUTC(region):
    if region in utc_5:
        return "UTC - 5"
    elif region in utc_4:
        return "UTC - 4"
    elif region in utc_3:
        return "UTC - 3"
    else:
        return "UTC - 2"

######################################################################
## FUNÇÕES PARA COLETA DE HORÁRIO, DATA E UTC | OBSERVATÓRIO NACIONAL
######################################################################
def curlDiaStr():
    url = 'http://www.horalegalbrasil.mct.on.br/RelogioServidor.php'
    return datetime.datetime.fromtimestamp(int(requests.get(url).text)).strftime('%d-%m-%Y')

def curlDiaUnix():
    url = 'http://www.horalegalbrasil.mct.on.br/RelogioServidor.php'
    return int(requests.get(url).text)

def curlDiaSemana():
    url = 'http://www.horalegalbrasil.mct.on.br/RelogioServidor.php'
    weekday = datetime.datetime.fromtimestamp(int(requests.get(url).text)).weekday()
    if weekday == 6: #Para adaptar para os padrões brasileiros, o domingo será zero, e o resto dos dias receberão +1
        return 0
    else:
        return weekday+1

def curlMes():
    url = 'http://www.horalegalbrasil.mct.on.br/RelogioServidor.php'
    return datetime.datetime.fromtimestamp(int(requests.get(url).text)).strftime('%m')

def curlDiaSemanaStr():
    url = 'http://www.horalegalbrasil.mct.on.br/RelogioServidor.php'
    weekday = datetime.datetime.fromtimestamp(int(requests.get(url).text)).weekday()
    if weekday == 0:
        return "Segunda-feira"
    elif weekday == 1:
        return "Terça-feira"
    elif weekday == 2:
        return "Quarta-feira"
    elif weekday == 3:
        return "Quinta-feira"
    elif weekday == 4:
        return "Sexta-feira"
    elif weekday == 5:
        return "Sábado"
    else:
        return "Domingo"

def curlHoraStr():
    url = 'http://www.horalegalbrasil.mct.on.br/RelogioServidor.php'
    return datetime.datetime.fromtimestamp(int(requests.get(url).text)).strftime('%d-%m-%Y %H:%M:%S')

def curlSomenteHoraStr():
    url = 'http://www.horalegalbrasil.mct.on.br/RelogioServidor.php'
    return datetime.datetime.fromtimestamp(int(requests.get(url).text)).strftime('%H:%M:%S')

def curlHoraDate():
    url = 'http://www.horalegalbrasil.mct.on.br/RelogioServidor.php'
    return datetime.datetime.fromtimestamp(int(requests.get(url).text))

def curlHoraInt():
    url = 'http://www.horalegalbrasil.mct.on.br/RelogioServidor.php'
    return int(requests.get(url).text)

def curlFuso():
    return datetime.datetime.fromtimestamp( curlHoraInt() + verificarUTC_num(geolocGP.region()) ).strftime('%d-%m-%Y %H:%M:%S') #Para testar outro estado, trocar "geoloc.region()" por "AC" ou outro estado de fuso horário diferente