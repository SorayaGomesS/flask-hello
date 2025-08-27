from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    # Página inicial simples, em inglês
    return "Hello, World!"

@app.route("/user/<name>")
def greet(name):
    # NÃO alteramos a capitalização: mostra exatamente o que vier na URL
    # Ex.: /user/Soraya%20Gomes -> "Hello, Soraya Gomes!"
    return f"Hello, {name}!"

# Importante: NÃO crie rota para /rotainexistente.
# Assim, acessar /rotainexistente resultará numa página 404 Not Found,
# exatamente como no exemplo das fotos.

# O bloco abaixo é ignorado no PythonAnywhere (a app roda via WSGI),
# mas não atrapalha estar aqui.
if __name__ == "__main__":
    app.run()
