from flask import Flask, render_template, redirect, request, url_for, session, flash
import mysql.connector
from mysql.connector import ClientFlag, Error
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'supersecretkey')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agendamentos')
def agendamentos():
    return render_template('agendamentos.html')

@app.route('/eventos', methods=['GET'])
def list_events():
    eventos = read_eventos()
    return render_template('eventos.html', eventos=eventos)

@app.route('/eventos', methods=['POST'])
def manage_events():
    if 'create' in request.form:
        if create_event():
            flash("Evento criado com sucesso!", "success")
        else:
            flash("Erro ao criar evento.", "error")
    elif 'update' in request.form:
        if update_event():
            flash("Evento atualizado com sucesso!", "success")
        else:
            flash("Erro ao atualizar evento.", "error")
    elif 'delete' in request.form:
        if delete_event():
            flash("Evento excluído com sucesso!", "success")
        else:
            flash("Erro ao excluir evento.", "error")
    
    eventos = read_eventos()
    return render_template('eventos.html', eventos=eventos)

@app.route('/instagram')
def instagram():
    return redirect('https://www.instagram.com/cscjuniorletal')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('nome')
        senha = request.form.get('senha')
        
        if login == "CSCJL1" and senha == "cscjl":
            session['loginStatus'] = True
            return redirect(url_for('eventos'))
        else:
            flash("Login ou senha inválidos.", "error")
            return redirect(url_for('login'))
    return render_template('adm.html')

def iniciaConexao():
    try:
        conexaoBanco = mysql.connector.connect(
            host=os.environ.get('DB_HOST', '127.0.0.1'),
            user=os.environ.get('DB_USER', 'root'),
            password=os.environ.get('DB_PASSWORD', 'P@ssAlun0'),
            database=os.environ.get('DB_NAME', 'protasete'),
            client_flags=[ClientFlag.PLUGIN_AUTH]
        )
        return conexaoBanco
    except Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

def create_event():
    nome = request.form.get('nome')
    imagem = request.form.get('imagem')
    descricao = request.form.get('descricao')
    dias = request.form.get('dias')

    if not nome or not imagem or not descricao or not dias:
        return False

    conexao = iniciaConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            comando = "INSERT INTO Evento (nome, imagem, descricao, dias) VALUES (%s, %s, %s, %s)"
            cursor.execute(comando, (nome, imagem, descricao, dias))
            conexao.commit()
            return True
        except Error as err:
            print(f"Erro ao criar evento: {err}")
            return False
        finally:
            cursor.close()
            conexao.close()
    return False

def delete_event():
    id = request.form.get('id')
    
    if not id:
        return False

    conexao = iniciaConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            comando = "DELETE FROM Evento WHERE id = %s"
            cursor.execute(comando, (id,))
            conexao.commit()
            return True
        except Error as err:
            print(f"Erro ao excluir evento: {err}")
            return False
        finally:
            cursor.close()
            conexao.close()
    return False

def update_event():
    id = request.form.get('id')
    nome = request.form.get('nome')
    imagem = request.form.get('imagem')
    descricao = request.form.get('descricao')
    dias = request.form.get('dias')

    if not id or not nome or not imagem or not descricao or not dias:
        return False

    conexao = iniciaConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            comando = "UPDATE Evento SET nome=%s, imagem=%s, descricao=%s, dias=%s WHERE id=%s"
            cursor.execute(comando, (nome, imagem, descricao, dias, id))
            conexao.commit()
            return True
        except Error as err:
            print(f"Erro ao atualizar evento: {err}")
            return False
        finally:
            cursor.close()
            conexao.close()
    return False

def read_eventos():
    conexao = iniciaConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM Evento;")
            eventos = cursor.fetchall()
            return eventos
        except Error as err:
            print(f"Erro ao ler eventos: {err}")
            return []
        finally:
            cursor.close()
            conexao.close()
    return []

if __name__ == '__main__':
    app.run(debug=True)