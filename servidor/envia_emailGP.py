import smtplib, os

def enviaEmailToken(token, email):
    # Pega variáveis do ambiente
    USER = os.getenv('API_USER')
    PASSWORD = os.environ.get('API_PASSWORD')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.connect("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(USER, PASSWORD)
    msg = '''Sua senha esta sendo reconfigurada, por favor, entre com o codigo abaixo\n\n\n\n'''+token
    server.sendmail(USER, email, msg.encode('utf-8'))