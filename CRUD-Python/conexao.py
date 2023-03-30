# vídeo de referencia: https://www.youtube.com/watch?v=_q3j25ACmQ4&t=1510s

#import mysql.connector

#conexao = mysql.connector.connect(
#    host='localhost',
#    user='root',
#    password='',
#    database='gestaoacademica',
#)

#cursor = conexao.cursor()

# DETELE
#cpf = 123456
#comando = f'DELETE FROM aluno WHERE cpf = {cpf}'
#cursor.execute(comando)
#conexao.commit() 

# UPDATE
#cpf = 123456
#matricula = 444444
#comando = f'UPDATE aluno SET matricula = {matricula} WHERE cpf = {cpf}'
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados

# READ
#comando = f'SELECT * FROM aluno'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)

# CREATE
#cpf = 123456
#matricula = 654321
#nome_aluno = "maria"
#curso = "ads"
#comando = f'INSERT INTO aluno (cpf, matricula,nome_aluno, curso) VALUES ({cpf}, {matricula},"{nome_aluno}", "{curso}")'
#cursor.execute(comando)
#conexao.commit()

#cursor.close()
#conexao.close()