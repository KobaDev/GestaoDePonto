import requests
import datetime
import geoloc
#import time

utc_5 = ['AC']
utc_4 = ['AM', 'MT', 'MS', 'RO', 'RR']
utc_3 = ['AL', 'AP', 'BA', 'CE', 'ES', 'GO', 'MA', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'SP', 'SC', 'SE', 'TO', 'DF']

def verificarUTC_num(region):
    if region in utc_5:
        return -7200 #Retira 2 horas do horário de Brasília
    elif region in utc_4:
        return -3600 #Retira 1 hora do horário de Brasília
    elif region in utc_3:
        return 0     #Horário de Brasília
    else:
        return 3600

def verificarUTC(region):
    if region in utc_5:
        return "UTC - 5"
    elif region in utc_4:
        return "UTC - 4"
    elif region in utc_3:
        return "UTC - 3"
    else:
        return "UTC - 2"

def curlHoraStr():
    url = 'http://www.horalegalbrasil.mct.on.br/RelogioServidor.php'
    return datetime.datetime.fromtimestamp(int(requests.get(url).text)).strftime('%Y-%m-%d %H:%M:%S')

def curlHoraDate():
    url = 'http://www.horalegalbrasil.mct.on.br/RelogioServidor.php'
    return datetime.datetime.fromtimestamp(int(requests.get(url).text))

def curlHoraInt():
    url = 'http://www.horalegalbrasil.mct.on.br/RelogioServidor.php'
    return int(requests.get(url).text)

def curlFuso():
    return datetime.datetime.fromtimestamp( curlHoraInt() + verificarUTC_num(geoloc.region()) ).strftime('%Y-%m-%d %H:%M:%S') #Para testar outro estado, trocar "geoloc.region()" por "AC" ou outro estado de fuso horário diferente
