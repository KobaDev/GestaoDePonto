################################################################
## IMPORT DE RECURSO PARA INTERAÇÃO COM GEOLOCALIZAÇÃO
################################################################
import requests
import urllib
import json

################################################################
## VERIFICA REGIÃO | POR MEIO DO IP DEFINE LOCALIZAÇÃO EXATA
################################################################
def region():
    ip_addr = requests.get('https://api.ipify.org').text
    request_url = urllib.request.Request('http://ip-api.com/json/' + ip_addr)
    request = urllib.request.urlopen(request_url).read()
    resposta = json.loads(request.decode('utf-8'))

    return str(resposta['region'])

################################################################
## VERIFICA PAÍS | POR MEIO DO IP, REGATA O PAÍS DO USUÁRIO
################################################################
def country():
    ip_addr = requests.get('https://api.ipify.org').text
    request_url = urllib.request.Request('http://ip-api.com/json/' + ip_addr)
    request = urllib.request.urlopen(request_url).read()
    resposta = json.loads(request.decode('utf-8'))

    return str(resposta['country'])