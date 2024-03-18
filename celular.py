import sqlite3

def conectar_db():
    return sqlite3.connect('celular.db')

def criar_tabela():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuario
                      (email TEXT, senha TEXT)''')
    conn.commit()
    conn.close()

def cadastrar_usuario(email, senha):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuario (email, senha) VALUES (?, ?)', (email, senha))
    conn.commit()
    conn.close()

def buscar_usuario(email):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuario WHERE email = ?', (email,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario
