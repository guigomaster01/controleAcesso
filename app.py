from flask import Flask, render_template, request, jsonify, redirect, url_for, send_file
import sqlite3
from datetime import datetime
import pandas as pd
import os

app = Flask(__name__)

# Banco de dados
DATABASE = 'onibus.db'
EXPORT_FOLDER = 'static/downloads'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS registros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                registro TEXT,
                tipo TEXT NOT NULL,
                movimentacao TEXT NOT NULL,
                prefixoColetivo TEXT,
                observacoes TEXT,
                data_hora TEXT NOT NULL
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                registro INTEGER UNIQUE NOT NULL,
                nome TEXT NOT NULL
            )
        ''')
        conn.commit()

@app.route('/')
def index():
    return render_template('registro.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    data = (
        request.form.get("nome"),
        request.form.get("registro"),
        request.form.get("tipo"),
        request.form.get("movimentacao"),
        request.form.get("prefixoColetivo"),
        request.form.get("observacoes"),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    try:
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO registros
            (nome, registro, tipo, movimentacao, prefixoColetivo, observacoes, data_hora)
            VALUES (?, ?, ?, ?, ?, ?, ?)''', data)
        conn.commit()
        conn.close()
        return jsonify({"success": True, "message": "Registro salvo com sucesso."})
    except Exception as e:
        return jsonify({"success": False, "message": f"Erro ao salvar registro: {str(e)}"})

@app.route('/buscar_funcionario')
def buscar_funcionario():
    registro = request.args.get('registro')
    conn = get_db_connection()
    funcionario = conn.execute('SELECT nome FROM funcionarios WHERE registro = ?', (registro,)).fetchone()
    conn.close()

    if funcionario:
        return jsonify({"success": True, "nome": funcionario['nome']})
    else:
        return jsonify({"success": False})

@app.route('/visualizar')
def visualizar():
    conn = get_db_connection()
    registros = conn.execute('SELECT * FROM registros ORDER BY data_hora DESC').fetchall()
    conn.close()
    return render_template('visualizar.html', registros=registros)

@app.route('/exportar_excel')
def exportar_excel():
    conn = get_db_connection()
    df = pd.read_sql_query('SELECT * FROM registros ORDER BY data_hora DESC', conn)
    conn.close()

    if df.empty:
        return jsonify({"success": False, "message": "Nenhum registro encontrado."})

    os.makedirs(EXPORT_FOLDER, exist_ok=True)
    file_path = os.path.join(EXPORT_FOLDER, f"registros_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")
    df.to_excel(file_path, index=False, engine='openpyxl')

    return send_file(file_path, as_attachment=True, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)