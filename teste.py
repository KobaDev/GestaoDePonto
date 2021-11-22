import sqlite3

banco = sqlite3.connect('banco_cadastroGP.db') 
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS banco_cadastroGP (primeiro_nome text,segundo_nome text,user_email text,senha text, admin integer,cargo text,matricula text)")
cursor.execute("SELECT matricula FROM banco_cadastroGP ORDER BY matricula DESC")

matricula_str = int(cursor.fetchone())+1
matricula = str(matricula_str).ljust(4, '0')

print(matricula)