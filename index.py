from flask import Flask, render_template, request, redirect, url_for, flash, Response
from busca_ativo import retorna_ativo
from flask_session import Session
from erros import previne_erro

app = Flask(__name__)
app.secret_key = 'key'

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

lista_de_ativos = []

# Página principal
@app.route('/')
def index():
    return render_template('index.html')


# Rota de criação dos dados
@app.route('/busca-ativo', methods=['POST','GET'])
def busca_ativo():

    nome = request.form['ativo']
    data_inicial = request.form['data-inicial']
    data_final = request.form['data-final']
    
    json = retorna_ativo(nome, data_inicial, data_final)
  
    if (previne_erro(json) != True) or (data_final==''):
        flash('Algum dado está errado')
        return redirect(url_for('index'))
    
    else:
        lista_de_ativos.clear()
        lista_de_ativos.append(json)

        return redirect(url_for('resultado'))


# Página resultado
@app.route('/resultado')
def resultado():
    return render_template('resultado.html', json_ativo=lista_de_ativos[0][0])

@app.route('/download-csv')
def download_csv():
    csv = lista_de_ativos[0][1]
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=Ativo.csv"})


app.run(debug=True)