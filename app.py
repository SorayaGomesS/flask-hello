from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

# Rota principal
@app.route("/")
def index():
    now = datetime.now()
    return render_template_string("""
        <h1>Hello World!</h1>
        <p>The local date and time is {{ now.strftime("%B %d, %Y %I:%M %p") }}.</p>
        <p>That was a few seconds ago.</p>
    """, now=now)

# Rota de usuário
@app.route("/user/<name>")
def user(name):
    return render_template_string("<h1>Hello, Soraya Gomes!</h1>", name=name)

# Página de erro 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template_string("<h1>Not Found</h1>"), 404

