from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
connection = sqlite3.connect("agenda.db", check_same_thread=False)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastrar_cliente", methods=["GET", "POST"])
def cadastrar_cliente():
    if request.method == "POST":
        # Lógica para cadastrar um cliente
        cursor = connection.cursor()
        cursor.execute("INSERT INTO clientes (nome, telefone) VALUES (?, ?)",
                       (request.form["nome"], request.form["telefone"]))
        connection.commit()
        return redirect(url_for("index"))
    return render_template("cadastrar_cliente.html")

@app.route("/agendar_servico", methods=["GET", "POST"])
def agendar_servico():
    if request.method == "POST":
        # Lógica para agendar um serviço
        cursor = connection.cursor()
        cursor.execute("INSERT INTO agendamentos (cliente_id, servico_id, data_hora) VALUES (?, ?, ?)",
                       (request.form["cliente_id"], request.form["servico_id"], request.form["data_hora"]))
        connection.commit()
        return redirect(url_for("index"))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.execute("SELECT * FROM servicos")
    servicos = cursor.fetchall()
    return render_template("agendar_servico.html", clientes=clientes, servicos=servicos)

@app.route("/confirmar_agendamento", methods=["GET", "POST"])
def confirmar_agendamento():
    if request.method == "POST":
        # Lógica para confirmar o agendamento
        return redirect(url_for("index"))
    return render_template("confirmar_agendamento.html")

if __name__ == "__main__":
    app.run(debug=True)
