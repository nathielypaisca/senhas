
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Página HTML simplificada para o exemplo
pagina = """
<h1>Resultado do acesso</h1>
<p>{{ mensagem }}</p>
<a href="/">Voltar ao login</a>
"""

@app.route("/")
def inicio():
    with open("index.html", encoding="utf-8") as arquivo:
        return arquivo.read()

@app.route("/login", methods=["POST"])
def login():
    senha = request.form.get("senha", "")

    # Senha de demonstração
    if senha == "Python@123":
        mensagem = "Acesso permitido! Sistema protegido."
    else:
        mensagem = "Acesso negado! Senha incorreta."

    return render_template_string(pagina, mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)
