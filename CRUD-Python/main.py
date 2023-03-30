import os #importando biblioteca os
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='gestaoacademica',
)

cursor = conexao.cursor()

def limpar():
    os.system('clear') or None #comando para limpar tela

def headercadastro():
    limpar()
    print("-----------------------------------")
    print("             CADASTRO")
    print("-----------------------------------\n")

def headeralterar():
    limpar()
    print("-----------------------------------")
    print("             ALTERAR")
    print("-----------------------------------\n")

def headerdelete():
    limpar()
    print("-----------------------------------")
    print("             DELETAR")
    print("-----------------------------------\n")

def headerconsulta():
    limpar()
    print("-----------------------------------")
    print("             CONSULTAR")
    print("-----------------------------------\n")

def mensagemcadastro():
    print("-----------------------------------")
    print("             CONCLUÍDO!")
    print("-----------------------------------\n")
    print("[1] Realizar novo cadastro \n[2] Voltar para o Menu Principal \n[3] Finalizar")

def mensagemalterar():
    print("-----------------------------------")
    print("             CONCLUÍDO!")
    print("-----------------------------------\n")
    print("[1] Realizar nova alteração \n[2] Voltar para o Menu Principal \n[3] Finalizar")

def mensagemdelete():
    print("-----------------------------------")
    print("             CONCLUÍDO!")
    print("-----------------------------------\n")
    print("[1] Excluir novamente \n[2] Voltar para o Menu Principal \n[3] Finalizar")

def mensagemconsulta():
    print("\n-----------------------------------\n")
    print("[1] Realizar nova consulta \n[2] Voltar para o Menu Principal \n[3] Finalizar")

def headerfinalizar():
	print("-----------------------------------")
	print("         VOLTE SEMPRE! :D")
	print("-----------------------------------\n")

def menu():
    limpar()
    print("-----------------------------------")
    print("         GESTÃO ACADÊMICA")
    print("-----------------------------------\n")
    print("Escolha um para continuar:\n")
    print("[1] Cadastrar \n[2] Alterar \n[3] Excluir \n[4] Consultar")

    escolha1 = int(input('Escolha: '))

    if escolha1 == 1:
        def cadastro():
            headercadastro()

            print("Deseja cadastrar novo(a):\n")
            print("[1] Aluno \n[2] Funcionário \n[3] Disciplina \n[4] Curso")
            escolha2 = int(input('Escolha: '))

            if escolha2 == 1:
                headercadastro()

                nome_aluno = input('Nome: ')
                matricula = input('Matrícula: ')
                cpf = input('CPF: ')
                curso = input('Curso: ')

                # CREATE
                comando = f'INSERT INTO aluno (cpf, matricula,nome_aluno, curso) VALUES ({cpf}, {matricula},"{nome_aluno}", "{curso}")'
                cursor.execute(comando)
                conexao.commit()

                mensagemcadastro()

                resp = int(input('Escolha: '))
									
                if resp == 1:
                    cadastro()
                elif resp == 2:
                    menu()
                elif resp == 3:
                    headerfinalizar()
                else:
                    print("Opção Inválida!")

            elif escolha2 == 2:
                headercadastro()

                nome = input('Nome: ')
                endereco = input('Endereço: ')
                telefone = input('Telefone: ')
                cpf = input('CPF: ')
                salario = float(input('Salário: R$'))
                print("Área de atuação:")
                print("[1] Professor \n[2] Técnico Administrativo")
                escolha3 = int(input('Escolha: '))

                if escolha3 == 1:
                    atuacao = 'Professor'
                    titulacao = input('Titulação: ')
                    formacao = input('Área de formação: ')

                    # CREATE
                    comando = f'INSERT INTO funcionario (cpf, nome, telefone, endereco, salario, atuacao, titulacao, formacao) VALUES ({cpf},"{nome}",{telefone},"{endereco}",{salario},"{atuacao}","{titulacao}", "{formacao}")'
                    cursor.execute(comando)
                    conexao.commit()

                elif escolha3 == 2:
                    atuacao = 'Técnico Administrativo'
                    titulacao = 'vazio'
                    formacao = 'vazio'

                    # CREATE
                    comando = f'INSERT INTO funcionario (cpf, nome, telefone, endereco, salario, atuacao, titulacao, formacao) VALUES ({cpf},"{nome}",{telefone},"{endereco}",{salario},"{atuacao}","{titulacao}", "{formacao}")'
                    cursor.execute(comando)
                    conexao.commit()

                else:
                    print("Opção Inválida!")

                mensagemcadastro()

                resp = int(input('Escolha: '))
									
                if resp == 1:
                    cadastro()
                elif resp == 2:
                    menu()
                elif resp == 3:
                    headerfinalizar()
                else:
                    print("Opção Inválida!")

            elif escolha2 == 3:
                headercadastro()

                codigo = input('Código: ')
                nome_disciplina = input('Nome: ')
                hora = int(input('Carga horária: '))
                cargahoraria = hora*10000

                # CREATE
                comando = f'INSERT INTO disciplina (codigo, nome_disciplina, cargahoraria) VALUES ({codigo},"{nome_disciplina}", {cargahoraria})'
                cursor.execute(comando)
                conexao.commit()

                mensagemcadastro()

                resp = int(input('Escolha: '))
									
                if resp == 1:
                    cadastro()
                elif resp == 2:
                    menu()
                elif resp == 3:
                    headerfinalizar()
                else:
                    print("Opção Inválida!")

            elif escolha2 == 4:
                headercadastro()

                codigo_curso = input('Código: ')
                nome_curso = input('Nome: ')
                data_inicio = input('Data-Início: ')
                data_fim =  input('Data-Fim: ')

                # CREATE
                comando = f'INSERT INTO curso (codigo_curso, nome_curso, data_inicio, data_fim) VALUES ({codigo_curso},"{nome_curso}", {data_inicio},{data_fim})'
                cursor.execute(comando)
                conexao.commit()

                mensagemcadastro()

                resp = int(input('Escolha: '))
									
                if resp == 1:
                    cadastro()
                elif resp == 2:
                    menu()
                elif resp == 3:
                    headerfinalizar()
                else:
                    print("Opção Inválida!")
            
            else:
                print("Opção Inválida!")

        cadastro()

    elif escolha1 == 2:
        def alterar():
            headeralterar()

            print("Deseja alterar:\n")
            print("[1] Aluno \n[2] Funcionário \n[3] Disciplina \n[4] Curso")
            escolha6 = int(input('Escolha: '))

            if escolha6 == 1:
                headeralterar()
    
                cpf = input('Informe o CPF: ')
                print("Deseja alterar:\n")
                print("[1] CPF \n[2] Matrícula \n[3] Nome \n[4] Curso")
                escolha7 = int(input('Escolha: '))

                if escolha7 == 1:

                    cpf_novo = input('Informe novo cpf: ')
              
                    # UPDATE
                    comando = f'UPDATE aluno SET cpf = {cpf_novo} WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                    cursor.execute(comando)
                    conexao.commit() #edita o banco de dados
                    
                elif escolha7 == 2:

                    matricula = input('Informe a nova matrícula: ')

                    # UPDATE
                    comando = f'UPDATE aluno SET matricula = {matricula} WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                    cursor.execute(comando)
                    conexao.commit() #edita o banco de dados

                elif escolha7 == 3:
                    
                    nome_aluno = input('Informe novo nome: ')

                    # UPDATE
                    comando = f'UPDATE aluno SET nome_aluno = "{nome_aluno}" WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                    cursor.execute(comando)
                    conexao.commit() #edita o banco de dados

                elif escolha7 == 4:

                    curso = input('Informe novo curso: ')

                    # UPDATE
                    comando = f'UPDATE aluno SET curso = "{curso}" WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                    cursor.execute(comando)
                    conexao.commit() #edita o banco de dados

                else:
                    print("Opção Inválida!")

                mensagemalterar()

                resp = int(input('Escolha: '))
                                        
                if resp == 1:
                    alterar()
                elif resp == 2:
                    menu()
                elif resp == 3:
                    headerfinalizar()
                else:
                    print("Opção Inválida!")

            elif escolha6 == 2:
                headeralterar()

                print("Professor ou Técnico Administrativo?\n")
                print("[1] Professor \n[2] Técnico Administrativo")
                escolha8 = int(input('Escolha: '))

                if escolha8 == 1:

                    cpf = input('Informe o cpf: ')
                    print("Deseja alterar:\n")
                    print("[1] CPF \n[2] Nome \n[3] Telefone \n[4] Endereço \n[5] Salário \n[6] Cargo \n[7] Titulação \n[8] Formação ")
                    escolha7 = int(input('Escolha: '))

                    if escolha7 == 1:

                        cpf_novo = input('Informe novo CPF: ')
                
                        # UPDATE
                        comando = f'UPDATE funcionario SET cpf = {cpf_novo} WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                        cursor.execute(comando)
                        conexao.commit() #edita o banco de dados

                    elif escolha7 == 2:
                        
                        nome = input('Informe novo nome: ')

                        # UPDATE
                        comando = f'UPDATE funcionario SET nome= "{nome}" WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                        cursor.execute(comando)
                        conexao.commit() #edita o banco de dados

                    elif escolha7 == 3:

                        telefone = input('Informe novo telefone: ')

                        # UPDATE
                        comando = f'UPDATE funcionario SET telefone = {telefone} WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                        cursor.execute(comando)
                        conexao.commit() #edita o banco de dados

                    elif escolha7 == 4:

                        endereco = input('Informe novo endereço: ')

                        # UPDATE
                        comando = f'UPDATE funcionario SET endereco = "{endereco}" WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                        cursor.execute(comando)
                        conexao.commit() #edita o banco de dados

                    elif escolha7 == 5:

                        salario = input('Informe novo salário: R$')

                        # UPDATE
                        comando = f'UPDATE funcionario SET salario = "{salario}" WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                        cursor.execute(comando)
                        conexao.commit() #edita o banco de dados
                    
                    elif escolha7 == 6:

                        print("Mudar para Técnico Administrativo?\n")
                        print("[1] Sim \n[2] Não")
                        escolha9 = int(input('Escolha: '))

                        if escolha9 == 1:
        
                            atuacao = "Técnico Administrativo"
                            titulacao = "vazio"
                            formacao = "vazio"

                            # UPDATE
                            comando = f'UPDATE funcionario SET atuacao = "{atuacao}", titulacao = "{titulacao}", formacao = "{formacao}" WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                            cursor.execute(comando)
                            conexao.commit() #edita o banco de dados 

                        elif escolha9 == 2:

                            mensagemalterar()

                            resp = int(input('Escolha: '))
                                                
                            if resp == 1:
                                alterar()
                            elif resp == 2:
                                menu()
                            elif resp == 3:
                                headerfinalizar()
                            else:
                                print("Opção Inválida!")
                        
                        else:
                            print("Opção Inválida!")
                    
                    elif escolha7 == 7:

                        titulacao = input('Informe nova titulação: ')

                        # UPDATE
                        comando = f'UPDATE funcionario SET titulacao = "{titulacao}" WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                        cursor.execute(comando)
                        conexao.commit() #edita o banco de dados

                    elif escolha7 == 8:

                        formacao = input('Informe nova formação: ')

                        # UPDATE
                        comando = f'UPDATE funcionario SET formacao = "{formacao}" WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                        cursor.execute(comando)
                        conexao.commit() #edita o banco de dados

                    else:
                        print("Opção Inválida!")

                    mensagemalterar()

                    resp = int(input('Escolha: '))
                                        
                    if resp == 1:
                        alterar()
                    elif resp == 2:
                        menu()
                    elif resp == 3:
                        headerfinalizar()
                    else:
                        print("Opção Inválida!")

                elif escolha8 == 2:

                    cpf = input('Informe o cpf: ')
                    print("Deseja alterar:\n")
                    print("[1] CPF \n[2] Nome \n[3] Telefone \n[4] Endereço \n[5] Salário \n[6] Cargo")
                    escolha7 = int(input('Escolha: '))

                    if escolha7 == 1:

                        cpf_novo = input('Informe novo CPF: ')
                
                        # UPDATE
                        comando = f'UPDATE funcionario SET cpf = {cpf_novo} WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                        cursor.execute(comando)
                        conexao.commit() #edita o banco de dados

                    elif escolha7 == 2:
                        
                        nome = input('Informe novo nome: ')

                        # UPDATE
                        comando = f'UPDATE funcionario SET nome= "{nome}" WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                        cursor.execute(comando)
                        conexao.commit() #edita o banco de dados

                    elif escolha7 == 3:

                        telefone = input('Informe novo telefone: ')

                        # UPDATE
                        comando = f'UPDATE funcionario SET telefone = {telefone} WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                        cursor.execute(comando)
                        conexao.commit() #edita o banco de dados

                    elif escolha7 == 4:

                        endereco = input('Informe novo endereço: ')

                        # UPDATE
                        comando = f'UPDATE funcionario SET endereco = "{endereco}" WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                        cursor.execute(comando)
                        conexao.commit() #edita o banco de dados

                    elif escolha7 == 5:

                        salario = input('Informe novo salário: ')

                        # UPDATE
                        comando = f'UPDATE funcionario SET salario = "{salario}" WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                        cursor.execute(comando)
                        conexao.commit() #edita o banco de dados
                    
                    elif escolha7 == 6:

                        print("Mudar para Professor?\n")
                        print("[1] Sim \n[2] Não")
                        escolha9 = int(input('Escolha: '))

                        if escolha9 == 1:
        
                            atuacao = "Professor"
                            titulacao = input('Titulação: ')
                            formacao = input('Área de formação: ')

                            # UPDATE
                            comando = f'UPDATE funcionario SET atuacao = "{atuacao}", titulacao = "{titulacao}", formacao = "{formacao}" WHERE cpf = {cpf}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                            cursor.execute(comando)
                            conexao.commit() #edita o banco de dados 

                        elif escolha9 == 2:

                            mensagemalterar()

                            resp = int(input('Escolha: '))
                                                
                            if resp == 1:
                                alterar()
                            elif resp == 2:
                                menu()
                            elif resp == 3:
                                headerfinalizar()
                            else:
                                print("Opção Inválida!")
                        
                        else:
                            print("Opção Inválida!")

                    else:
                        print("Opção Inválida!")


                    mensagemalterar()

                    resp = int(input('Escolha: '))
                                                
                    if resp == 1:
                        alterar()
                    elif resp == 2:
                            menu()
                    elif resp == 3:
                        headerfinalizar()
                    else:
                        print("Opção Inválida!")

                else:
                    print("Opção Inválida!")

            elif escolha6 == 3:

                codigo = input('Informe o código: ')
                print("Deseja alterar:\n")
                print("[1] Código \n[2] Nome \n[3] Carga Horária")
                escolha10 = int(input('Escolha: '))

                if escolha10 == 1:

                    codigo_novo = input('Informe novo código: ')
              
                    # UPDATE
                    comando = f'UPDATE disciplina SET codigo = {codigo_novo} WHERE codigo = {codigo}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                    cursor.execute(comando)
                    conexao.commit() #edita o banco de dados
                    
                elif escolha10 == 2:

                    nome_disciplina = input('Informe novo nome: ')

                    # UPDATE
                    comando = f'UPDATE disciplina SET nome_disciplina = "{nome_disciplina}" WHERE codigo = {codigo}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                    cursor.execute(comando)
                    conexao.commit() #edita o banco de dados

                elif escolha10 == 3:
                    
                    hora = int(input('Informe nova carga horária: '))
                    cargahoraria = hora*10000

                    # UPDATE
                    comando = f'UPDATE disciplina SET cargahoraria = {cargahoraria} WHERE codigo = {codigo}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                    cursor.execute(comando)
                    conexao.commit() #edita o banco de dados

                else:
                    print("Opção Inválida!")

                mensagemalterar()

                resp = int(input('Escolha: '))
                                        
                if resp == 1:
                    alterar()
                elif resp == 2:
                    menu()
                elif resp == 3:
                    headerfinalizar()
                else:
                    print("Opção Inválida!")

            elif escolha6 == 4:

                codigo_curso = input('Informe o código: ')
                print("Deseja alterar:\n")
                print("[1] Código \n[2] Nome \n[3] Data-inicio \n[4] Data-fim")
                escolha10 = int(input('Escolha: '))

                if escolha10 == 1:

                    codigo_novo = input('Informe novo código: ')
              
                    # UPDATE
                    comando = f'UPDATE curso SET codigo_curso = {codigo_novo} WHERE codigo_curso = {codigo_curso}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                    cursor.execute(comando)
                    conexao.commit() #edita o banco de dados
                    
                elif escolha10 == 2:

                    nome_curso = input('Informe novo nome: ')

                    # UPDATE
                    comando = f'UPDATE curso SET nome_curso = "{nome_curso}" WHERE codigo_curso = {codigo_curso}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                    cursor.execute(comando)
                    conexao.commit() #edita o banco de dados

                elif escolha10 == 3:
                    
                    data_inicio = input('Informe nova Data-inicio: ')

                    # UPDATE
                    comando = f'UPDATE curso SET data_inicio = {data_inicio} WHERE codigo_curso = {codigo_curso}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                    cursor.execute(comando)
                    conexao.commit() #edita o banco de dados

                elif escolha10 == 4:
                    
                    data_fim = input('Informe Data-fim: ')

                    # UPDATE
                    comando = f'UPDATE curso SET data_fim = {data_fim} WHERE codigo_curso = {codigo_curso}' #passa a tabela, dps o valor que vai editar, e dps em quais linhas - identificando pela pk
                    cursor.execute(comando)
                    conexao.commit() #edita o banco de dados

                else:
                    print("Opção Inválida!")

                mensagemalterar()

                resp = int(input('Escolha: '))
                                        
                if resp == 1:
                    alterar()
                elif resp == 2:
                    menu()
                elif resp == 3:
                    headerfinalizar()
                else:
                    print("Opção Inválida!")
            
            else:
                print("Opção Inválida!")

        alterar()

    elif escolha1 == 3:
        def excluir():
            headerdelete()

            print("Deseja excluir:\n")
            print("[1] Aluno \n[2] Funcionário \n[3] Disciplina \n[4] Curso")
            escolha4 = int(input('Escolha: '))
            
            if escolha4 == 1:
                # DETELE
                cpf = input('Informe o cpf: ')
                comando = f'DELETE FROM aluno WHERE cpf = {cpf}'
                cursor.execute(comando)
                conexao.commit()

                mensagemdelete()

                resp = int(input('Escolha: '))
                                        
                if resp == 1:
                    excluir()
                elif resp == 2:
                    menu()
                elif resp == 3:
                    headerfinalizar()
                else:
                    print("Opção Inválida!")

            elif escolha4 == 2:
                # DETELE
                cpf = input('Informe o cpf: ')
                comando = f'DELETE FROM funcionario WHERE cpf = {cpf}'
                cursor.execute(comando)
                conexao.commit()

                mensagemdelete()

                resp = int(input('Escolha: '))
                                        
                if resp == 1:
                    excluir()
                elif resp == 2:
                    menu()
                elif resp == 3:
                    headerfinalizar()
                else:
                    print("Opção Inválida!")

            elif escolha4 == 3:
                # DETELE
                codigo = input('Informe o código: ')
                comando = f'DELETE FROM disciplina WHERE codigo = {codigo}'
                cursor.execute(comando)
                conexao.commit()

                mensagemdelete()

                resp = int(input('Escolha: '))
                                        
                if resp == 1:
                    excluir()
                elif resp == 2:
                    menu()
                elif resp == 3:
                    headerfinalizar()
                else:
                    print("Opção Inválida!")

            elif escolha4 == 4:
                # DETELE
                codigo_curso = input('Informe o código: ')
                comando = f'DELETE FROM curso WHERE codigo_curso = {codigo_curso}'
                cursor.execute(comando)
                conexao.commit()

                mensagemdelete()

                resp = int(input('Escolha: '))
                                        
                if resp == 1:
                    excluir()
                elif resp == 2:
                    menu()
                elif resp == 3:
                    headerfinalizar()
                else:
                    print("Opção Inválida!")
                           
            else:
                print("Opção Inválida!")

        excluir()

    elif escolha1 == 4:
        def consulta():
            headerconsulta()

            print("Deseja consultar:\n")
            print("[1] Alunos \n[2] Funcionários \n[3] Disciplinas \n[4] Cursos")
            escolha5 = int(input('Escolha: '))

            if escolha5 == 1:
                # READ
                comando = f'SELECT * FROM aluno'
                cursor.execute(comando)
                resultado = cursor.fetchall()
                print("CPF | Matrícula | Nome | Curso\n")
                print(resultado)
            
                mensagemconsulta()

                resp = int(input('Escolha: '))
                                            
                if resp == 1:
                    consulta()
                elif resp == 2:
                    menu()
                elif resp == 3:
                    headerfinalizar()
                else:
                    print("Opção Inválida!")

            elif escolha5 == 2:
                # READ
                comando = f'SELECT * FROM funcionario'
                cursor.execute(comando)
                resultado = cursor.fetchall()
                print("CPF | Nome | Telefone | Endereço | Salário | Cargo | Titulação | Formação\n")
                print(resultado)

                mensagemconsulta()

                resp = int(input('Escolha: '))
                                            
                if resp == 1:
                    consulta()
                elif resp == 2:
                    menu()
                elif resp == 3:
                    headerfinalizar()
                else:
                    print("Opção Inválida!")

            elif escolha5 == 3:
                # READ
                comando = f'SELECT * FROM disciplina'
                cursor.execute(comando)
                resultado = cursor.fetchall()
                print("Código | Nome | Carga Horária\n")
                print(resultado) 

                mensagemconsulta()

                resp = int(input('Escolha: '))
                                            
                if resp == 1:
                    consulta()
                elif resp == 2:
                    menu()
                elif resp == 3:
                    headerfinalizar()
                else:
                    print("Opção Inválida!")
            
            elif escolha5 == 4:
                # READ
                comando = f'SELECT * FROM curso'
                cursor.execute(comando)
                resultado = cursor.fetchall()
                print("Código | Nome | Data-Início | Data-Fim\n")
                print(resultado)

                mensagemconsulta()

                resp = int(input('Escolha: '))
                                            
                if resp == 1:
                    consulta()
                elif resp == 2:
                    menu()
                elif resp == 3:
                    headerfinalizar()
                else:
                    print("Opção Inválida!")

            else:
                print("Opção Inválida!")

        consulta()

    else:
        print("Opção Inválida!")
        
menu()

cursor.close()
conexao.close()