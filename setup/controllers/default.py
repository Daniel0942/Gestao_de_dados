from setup import app
from flask import render_template, redirect, url_for, request, flash, session
from setup.models.table import Conexao

# Rota do login
@app.route("/")
def login_index():
    return render_template("login.html")

@app.route("/", methods=["POST"])
def logar_usuario():
    username = request.form["username"]
    password = request.form["password"]

    conectar = Conexao()
    cursor = conectar.cursor(dictionary=True)
    cursor.execute("SELECT username, password FROM users WHERE username = %s", (username,))
    lista = cursor.fetchone()

    if lista["username"] == username and lista["password"] == password:
        print("Logado com sucesso")
        session["username"] = username
        return redirect(url_for("dados_index"))
    else:
        print("Usuário ou senha incorretos !")
        return redirect(url_for("login_index"))
    
# Rota do registrar
@app.route("/registrar")
def registrar_index():
    return render_template("registrar.html")

@app.route("/registrar", methods=["POST"])
def registrar_usuario():
    username = request.form["username"]
    password = request.form["password"]
    
    conectar = Conexao()
    cursor = conectar.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conectar.commit()
    cursor.close()
    conectar.close()
    return render_template("login.html", username=username, password=password)

# Rota dos dados
@app.route("/dados")
def dados_index():
    username = session["username"]
    conectar = Conexao()
    cursor = conectar.cursor(dictionary=True)
    cursor.execute("SELECT * FROM dados WHERE username = %s", (username,))
    data = cursor.fetchall()
    #data = data[0]
    cursor.close()
    conectar.close()
    return render_template("dados.html", dados = data)

@app.route("/dados", methods=["POST"])
def adicionar_dados():
    titulo = request.form["titulo"]
    msg = request.form["msg"]
    username = session["username"]
    
    conectar = Conexao()
    cursor = conectar.cursor()
    cursor.execute("INSERT INTO dados (username, titulo, msg) VALUES (%s, %s, %s)", (username, titulo, msg))
    conectar.commit()
    cursor.close()
    conectar.close()

    return redirect(url_for("dados_index"))

@app.route("/dados/<int:username_id>", methods=["GET"])
def form_edit_dados(username_id):
    conectar = Conexao()
    cursor = conectar.cursor(dictionary=True)
    cursor.execute("SELECT titulo, msg FROM dados WHERE id = %s", (username_id,))
    dados = cursor.fetchall()
    dados = dados[0]

    data = {
        "username_id": username_id,
        "titulo": dados["titulo"],
        "msg": dados["msg"]
    }
    cursor.close()
    conectar.close()
    return render_template("dados.html", dados_edit = data)

@app.route("/dados/<int:username_id>", methods=["POST"])
def editar_dados(username_id):
    if request.form.get('_method') == 'PUT':

        titulo = request.form["titulo"]
        msg = request.form["msg"]

        conectar = Conexao()
        cursor = conectar.cursor()
        cursor.execute("UPDATE dados SET titulo = %s, msg = %s WHERE id = %s", (titulo, msg, username_id))
        conectar.commit()
        cursor.close()
        conectar.close()
        return redirect(url_for("dados_index"))

@app.route("/dados/deletar/<int:username_id>", methods=["GET"])
def deletar_dados(username_id):
    conectar = Conexao()
    cursor = conectar.cursor()
    cursor.execute("DELETE FROM dados WHERE id = %s", (username_id,))
    conectar.commit()
    cursor.close()
    conectar.close()
    return redirect(url_for("dados_index"))