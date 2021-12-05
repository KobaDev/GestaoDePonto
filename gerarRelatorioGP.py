import datetime, pega_horarioGP, sqlite3, time
from tkinter.filedialog import askdirectory

def gerarArquivo(nome, matricula, data_inicial_unix, data_final_unix, mesma_data):
    path = askdirectory(title='Salvar como...') #Abre uma janela para a escolha do diretório

    if not path:    return 0 #Retorna 0 se o usuário cancelar a ação

    conteudo = [
    "Nome do Funcionário: "+nome+"\n",
    "Matrícula: "+matricula+"\n",
    "Horario              Pontos               Marcação             Justificativa".ljust(60),
    ""]

    data_str = datetime.datetime.fromtimestamp(int(data_inicial_unix)).strftime('%d-%m-%Y')

    banco = sqlite3.connect('banco_pontoGP.db') 
    cursor = banco.cursor()
    try:
        if mesma_data == True:
            cursor.execute("SELECT data,hora,entrada,justificativa FROM banco_pontoGP WHERE data == '"+data_str+"' AND matricula = '"+matricula+"' ORDER BY data_unix ASC")
        else:
            cursor.execute("SELECT data,hora,entrada,justificativa FROM banco_pontoGP WHERE data_unix BETWEEN "+data_inicial_unix+" AND "+data_final_unix+" AND matricula = '"+matricula+"' ORDER BY data_unix ASC")
    except sqlite3.Error as erro:
        return ("Erro ao pesquisar os dados: "+str(erro))

    pontos = cursor.fetchall()
    banco.close()

    for x in range(0, len(pontos)):
        conteudo[3] += "\n- "+pontos[x][0].ljust(15) +"    - "+ pontos[x][1].ljust(15) +"    - "+ pontos[x][2].ljust(15) +"    - "+ pontos[x][3].ljust(15)

    arquivo = ""
    arquivo = path + "\\relatorio_" + pega_horarioGP.curlDiaStr() + "_" + matricula + ".txt" #Define nome e caminho do arquivo

    with open(arquivo, "w", encoding='utf8') as f:
        for line in conteudo:
            f.write(f'{line}\n')
    f.close()
    return 1



def gerarArquivoDia(nome, matricula):
    path = askdirectory(title='Salvar como...') #Abre uma janela para a escolha do diretório

    if not path:    return 0 #Retorna 0 se o usuário cancelar a ação

    conteudo = [
    "Nome do Funcionário: "+nome+"\n",
    "Matrícula: "+matricula+"\n",
    "Horario              Pontos               Marcação             Justificativa".ljust(60),
    ""]

    banco = sqlite3.connect('banco_pontoGP.db') 
    cursor = banco.cursor()

    try:
        cursor.execute("SELECT data,hora,entrada,justificativa FROM banco_pontoGP WHERE data == '"+pega_horarioGP.curlDiaStr()+"' AND matricula = '"+matricula+"' ORDER BY data_unix ASC")
    except sqlite3.Error as erro:
        return ("Erro ao pesquisar os dados: "+str(erro))

    pontos = cursor.fetchall()
    banco.close()

    for x in range(0, len(pontos)):
        conteudo[3] += "\n- "+pontos[x][0].ljust(15) +"    - "+ pontos[x][1].ljust(15) +"    - "+ pontos[x][2].ljust(15) +"    - "+ pontos[x][3].ljust(15)

    arquivo = ""
    arquivo = path + "\\relatorio_" + pega_horarioGP.curlDiaStr() + "_" + matricula + "_DIA.txt" #Define nome e caminho do arquivo

    with open(arquivo, "w", encoding='utf8') as f:
        for line in conteudo:
            f.write(f'{line}\n')
    f.close()
    return 1



def gerarArquivoSemana(nome, matricula):
    path = askdirectory(title='Salvar como...') #Abre uma janela para a escolha do diretório

    if not path:    return 0 #Retorna 0 se o usuário cancelar a ação

    conteudo = [
    "Nome do Funcionário: "+nome+"\n",
    "Matrícula: "+matricula+"\n",
    "Horario              Pontos               Marcação             Justificativa".ljust(60),
    ""]

    data_final_unix = pega_horarioGP.curlDiaUnix()
    data_inicial_unix = data_final_unix - (pega_horarioGP.curlDiaSemana() * 24*60*60) #Subtrai o número de dias da semana pra obter o começo dela p/ a data inicial

    banco = sqlite3.connect('banco_pontoGP.db') 
    cursor = banco.cursor()
    try:
        if data_final_unix == data_inicial_unix:
            cursor.execute("SELECT data,hora,entrada,justificativa FROM banco_pontoGP WHERE data == '"+pega_horarioGP.curlDiaStr()+"' AND matricula = '"+matricula+"' ORDER BY data_unix ASC")
        else:
            cursor.execute("SELECT data,hora,entrada,justificativa FROM banco_pontoGP WHERE data_unix BETWEEN "+str(data_inicial_unix)+" AND "+str(data_final_unix)+" AND matricula = '"+matricula+"' ORDER BY data_unix ASC")
    except sqlite3.Error as erro:
        return ("Erro ao pesquisar os dados: "+str(erro))

    pontos = cursor.fetchall()
    banco.close()

    for x in range(0, len(pontos)):
        conteudo[3] += "\n- "+pontos[x][0].ljust(15) +"    - "+ pontos[x][1].ljust(15) +"    - "+ pontos[x][2].ljust(15) +"    - "+ pontos[x][3].ljust(15)

    arquivo = ""
    arquivo = path + "\\relatorio_" + pega_horarioGP.curlDiaStr() + "_" + matricula + "_SEMANA.txt" #Define nome e caminho do arquivo

    with open(arquivo, "w", encoding='utf8') as f:
        for line in conteudo:
            f.write(f'{line}\n')
    f.close()
    return 1


def gerarArquivoMes(nome, matricula):
    path = askdirectory(title='Salvar como...') #Abre uma janela para a escolha do diretório

    if not path:    return 0 #Retorna 0 se o usuário cancelar a ação

    conteudo = [
    "Nome do Funcionário: "+nome+"\n",
    "Matrícula: "+matricula+"\n",
    "Horario              Pontos               Marcação             Justificativa".ljust(60),
    ""]

    banco = sqlite3.connect('banco_pontoGP.db') 
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT data,hora,entrada,justificativa FROM banco_pontoGP WHERE data LIKE '%-"+pega_horarioGP.curlMes()+"-2021' AND matricula = '"+matricula+"' ORDER BY data_unix ASC")
    except sqlite3.Error as erro:
        return ("Erro ao pesquisar os dados: "+str(erro))

    pontos = cursor.fetchall()
    banco.close()

    for x in range(0, len(pontos)):
        conteudo[3] += "\n- "+pontos[x][0].ljust(15) +"    - "+ pontos[x][1].ljust(15) +"    - "+ pontos[x][2].ljust(15) +"    - "+ pontos[x][3].ljust(15)

    arquivo = ""
    arquivo = path + "\\relatorio_" + pega_horarioGP.curlDiaStr() + "_" + matricula + "_MES.txt" #Define nome e caminho do arquivo

    with open(arquivo, "w", encoding='utf8') as f:
        for line in conteudo:
            f.write(f'{line}\n')
    f.close()
    return 1