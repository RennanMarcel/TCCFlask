from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agendamentos')
def agendamentos():
    return render_template('agendamentos.html')

@app.route('/fale_conosco')
def fale_conosco():
        return render_template('contate-nos.html')


@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/adm')
def adm():
        return render_template('adm.html')

if __name__ == '__main__':
    app.run(debug=True)