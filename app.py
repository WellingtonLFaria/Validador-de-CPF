from flask import Flask, render_template, request
from validador_de_cpf import validador

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        return render_template("index.html", validacao=validador(request.form['cpf'])) if request.form['cpf'] != "" else render_template("index.html", validacao="Campo Vazio")

if __name__ == "__main__":
    app.run(host='0.0.0.0')