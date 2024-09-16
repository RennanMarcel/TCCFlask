from flask import Flask, render_template, redirect, request, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessário para usar sessões

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agendamentos')
def agendamentos():
    if 'loginStatus' not in session:
        return redirect(url_for('login'))
    return render_template('agendamentos.html')

@app.route('/fale_conosco')
def fale_conosco():
    return render_template('contate-nos.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

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
            return redirect(url_for('login'))
    return render_template('adm.html')

if __name__ == '__main__':
    app.run(debug=True)
