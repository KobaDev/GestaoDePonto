import datetime, pega_horarioGP, sqlite3, time
from tkinter.filedialog import askdirectory

def gerarArquivo(nome, matricula, data_inicial_unix, data_final_unix):
    path = askdirectory(title='Salvar como...') # shows dialog box and return the path

    conteudo = [
    "Nome do Funcionário: "+nome+"\n",
    "Matrícula: "+matricula+"\n",
    "Horario              Pontos               Marcação             Justificativa".ljust(60),
    ""]

    banco = sqlite3.connect('banco_pontoGP.db') 
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT data,hora,entrada,justificativa FROM banco_pontoGP WHERE data_unix BETWEEN "+data_inicial_unix+" AND "+data_final_unix+" AND matricula = '"+matricula+"' ORDER BY data_unix ASC")
    except sqlite3.Error as erro:
            print("Erro ao pesquisar os dados: "+str(erro))

    pontos = cursor.fetchall()
    banco.close()

    for x in range(0, len(pontos)):
        conteudo[3] += "\n- "+pontos[x][0].ljust(15) +"    - "+ pontos[x][1].ljust(15) +"    - "+ pontos[x][2].ljust(15) +"    - "+ pontos[x][3].ljust(15)

    arquivo = ""
    arquivo = path + "\\relatorio_" + pega_horarioGP.curlDiaStr() + "_" + matricula + ".txt"

    with open(arquivo, "w", encoding='utf8') as f:
        for line in conteudo:
            f.write(f'{line}\n')
    f.close()
    return