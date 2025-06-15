import sqlite3

def conectar():
    return sqlite3.connect('ong.db')

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS beneficiarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            endereco TEXT,
            documento TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            beneficiario_id INTEGER,
            item TEXT,
            quantidade INTEGER,
            data TEXT,
            FOREIGN KEY (beneficiario_id) REFERENCES beneficiarios(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS voluntarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            area_atuacao TEXT
        )
    ''')

    conn.commit()
    conn.close()