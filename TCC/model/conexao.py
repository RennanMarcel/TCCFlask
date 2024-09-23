import mysql.connector

def iniciaConexao():
    conexaoBanco = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="P@ssAlun0",
      database="protasete"
    )
    return conexaoBanco


def createEvento(nome, descricao, dias): 
    conexao = iniciaConexao()
    cursor = conexao.cursor()
    comando = "INSERT INTO evento (nome, descricao, dias) VALUES(%s, %s, %s)"
    valores = [nome, descricao, dias]
    cursor.execute(comando, valores)
    conexao.commit() # edita o banco de dados
    #resultado= cursor.fetchtall() #ler o banco de dados
    print("Evento cadastrado com sucesso")
    cursor.close()
    conexao.close()

def deleteEvento(id):    
    conexao = iniciaConexao()
    cursor = conexao.cursor()
    comando = "DELETE FROM evento WHERE id = %s"
    valores = [id]
    cursor.execute(comando, valores)
    conexao.commit() # edita o banco de dados
    #resultado= cursor.fetchtall() #ler o banco de dados
    print("Evento excluido com sucesso")
    cursor.close()
    conexao.close()


def updateEvento(nome,imagem,descricao,dias,id):
     conexao = iniciaConexao()
     cursor = conexao.cursor()
     comando = "UPDATE evento SET nome=%s,imagem = %s,dias = %s, descricao = %s WHERE id= %i"
     valores = [nome,imagem,descricao,dias,id]
     cursor.execute(comando, valores)
     conexao.commit() # edita o banco de dados
        #resultado= cursor.fetchtall() #ler o banco de dados
     print("Evento atualizado com sucesso")
     cursor.close()
     conexao.close()


def readcardapio():
    conexao = iniciaConexao()
    cursor = conexao.cursor()
    comando = "SELECT * FROM evento;"
    cursor.execute(comando)
    eventos = cursor.fetchall()
    eventos_list = []
    for evento in eventos:
        eventos_list.append({
            'nome': evento[1],
            'imagem': evento[2],
            'descricao': evento[3],
            'dias': evento[4]
        })
        cursor.close()
        conexao.close()
    return eventos_list
    conexao.commit() # edita o banco de dados
    #resultado= cursor.fetchtall() #ler o banco de dados
    print("Evento")