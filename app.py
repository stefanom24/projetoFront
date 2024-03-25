from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index/voltar")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/index/login")
def login():
    return render_template("login.html")

@app.route("/index/login-result")
def login_result():
    username = request.args.get('username')
    
    return f"<h1>Login feito com sucesso!</h1><br>Username: {username}<br>"

@app.route("/index/trens")
def trens():
    return render_template("trens.html")

@app.route("/index/linhas")
def linhas():
    return render_template("linhas.html")

@app.route("/index/estacoes")
def estacoes():
    return render_template("estacoes.html")

@app.route("/index/mapa")
def mapa():
    return render_template("mapa.html")

@app.route("/index/ocorrencias")
def ocorrencias():
    return render_template("ocorrencias.html")
