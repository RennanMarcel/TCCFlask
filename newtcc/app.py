from flask import Flask, render_template, redirect, request, url_for, session, flash
import mysql.connector
from mysql.connector import ClientFlag, Error
import os
from model import conexao

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'supersecretkey')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agendamentos')
def agendamentos():
    return render_template('agendamentos.html')

@app.route('/fale_conosco')
def fale_conosco():
    return render_template('contate-nos.html')

@app.route('/eventos', methods=['GET', 'POST'])
def eventos():
    return render_template('eventos.html')

@app.post('/eventos/criar')
def CriandoEvento():
    nome_evento = request.form['nome']
    descricao = request.form['descricao']
    data = request.form['dias']
    
    conexao.createEvento(nome_evento, descricao, data)
    return redirect(url_for('eventos'))
    

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

if __name__ == '__main__':
    app.run(debug=True)