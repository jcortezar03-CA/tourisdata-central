import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'clave_secreta_123')

DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE usuario=? AND contrasena=?", (usuario, contrasena))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['usuario'] = usuario
            return redirect(url_for('menu'))
        else:
            error = 'Usuario o contraseña incorrectos'
    return render_template('login.html', error=error)

@app.route('/menu')
def menu():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('menu.html', usuario=session['usuario'])

@app.route('/dashboard1')
def dashboard1():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard1.html')

@app.route('/dashboard2')
def dashboard2():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard2.html')

@app.route('/dashboard3')
def dashboard3():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard3.html')

@app.route('/dashboard4')
def dashboard4():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard4.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
