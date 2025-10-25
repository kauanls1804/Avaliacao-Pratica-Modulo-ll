import sqlite3

conexao = sqlite3.connect('escola1.db')

cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
	id INTEGER PRIMARY KEY AUTOINCREMENT,   
	nome TEXT NOT NULL,
	idade INTEGER,
	email TEXT NOT NULL         
)
''')     

#cursor.execute("INSERT INTO alunos ('nome', 'idade', 'email') VALUES (?,?,?)", ('mirelly' , 17 , 'mirellybonardo@gmail.com'))
conexao.commit()
conexao.close()

conexao = sqlite3.connect('escola1.db')
cursor = conexao.cursor()

colsulta = cursor.execute('SELECT * FROM alunos')
    

for lista in colsulta.fetchall():
	print(f' nome: {lista[1]} | idade: {lista[2]} | email: {lista[3]}:.2f')


cursor.execute("UPDATE alunos SET idade = ? WHERE id = ?", ('18', 2))
conexao.commit()


cursor.execute("DELETE FROM alunos WHERE id =?", (7,))
conexao.commit()
conexao.close()

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

