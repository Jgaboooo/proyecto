from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definir el modelo de la base de datos
class ExampleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catastrofes')
def nosotros():
    return render_template('catastrofes.html')

@app.route('/soluciones')
def soluciones():
    return render_template('soluciones.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        return redirect(url_for('index'))
    return render_template('form.html')

@app.route('/bot')
def bot():
    return render_template('bot.html')

if __name__ == '__main__':
    app.run(debug=True)
