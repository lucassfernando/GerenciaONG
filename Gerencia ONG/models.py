from database import conectar
import csv

# BENEFICIÁRIOS
def adicionar_beneficiario(nome, telefone, endereco, documento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO beneficiarios (nome, telefone, endereco, documento) VALUES (?, ?, ?, ?)",
                   (nome, telefone, endereco, documento))
    conn.commit()
    conn.close()

def listar_beneficiarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM beneficiarios")
    dados = cursor.fetchall()
    conn.close()
    return dados

def deletar_beneficiario(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM beneficiarios WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def gerar_csv_beneficiarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM beneficiarios")
    dados = cursor.fetchall()
    conn.close()
    with open("relatorio_beneficiarios.csv", "w", newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Nome", "Telefone", "Endereço", "Documento"])
        writer.writerows(dados)

# DOAÇÕES
def adicionar_doacao(beneficiario_id, item, quantidade, data):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO doacoes (beneficiario_id, item, quantidade, data) VALUES (?, ?, ?, ?)",
                   (beneficiario_id, item, quantidade, data))
    conn.commit()
    conn.close()

def listar_doacoes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT d.id, b.nome, d.item, d.quantidade, d.data FROM doacoes d JOIN beneficiarios b ON d.beneficiario_id = b.id")
    dados = cursor.fetchall()
    conn.close()
    return dados

def gerar_csv_doacoes():
    doacoes = listar_doacoes()
    with open("relatorio_doacoes.csv", "w", newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Beneficiário", "Item", "Quantidade", "Data"])
        writer.writerows(doacoes)

# VOLUNTÁRIOS
def adicionar_voluntario(nome, telefone, area_atuacao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO voluntarios (nome, telefone, area_atuacao) VALUES (?, ?, ?)",
                   (nome, telefone, area_atuacao))
    conn.commit()
    conn.close()

def listar_voluntarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM voluntarios")
    dados = cursor.fetchall()
    conn.close()
    return dados

def gerar_csv_voluntarios():
    voluntarios = listar_voluntarios()
    with open("relatorio_voluntarios.csv", "w", newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Nome", "Telefone", "Área de Atuação"])
        writer.writerows(voluntarios)