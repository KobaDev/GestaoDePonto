import smtplib, os, autenticador_gen

def enviaEmailToken():
    # Pega variáveis do ambiente
    USER = os.getenv('API_USER')
    PASSWORD = os.environ.get('API_PASSWORD')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.connect("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(USER, PASSWORD)
    msg = '''Sua senha está sendo reconfigurada, por favor, entre com o código abaixo\n\n\n\n'''+autenticador_gen.generate_key()
    server.sendmail("kobashigawarenatoeinstein@gmail.com", "kobashigawarenato@gmail.com", msg.encode('utf-8'))