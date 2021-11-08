def gerarArquivo(path, conteudo):
    with open(path, "w", encoding='utf8') as f:
        for line in conteudo:
            f.write(f'{line}\n')
    f.close()


#Teste da função
v = ["Matrícula: 0001",
"Nome do Funcionário: Jadson Nascimento",
"Horario  Pontos  Justificativa",
"\
12/11/2021 13:45 | Entrada | Bla bla bla\n\
12/11/2021 13:45 | Almoco  | Bla bla bla\n\
12/11/2021 13:45 | Retorno | Bla bla bla\n\
12/11/2021 13:45 | Saida   | Bla bla bla\n\
"]

gerarArquivo("teste.txt", v)