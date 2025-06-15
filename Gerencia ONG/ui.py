import tkinter as tk
from tkinter import ttk, messagebox
from models import (
    adicionar_beneficiario, listar_beneficiarios, deletar_beneficiario,
    adicionar_doacao, listar_doacoes,
    adicionar_voluntario, listar_voluntarios,
    gerar_csv_beneficiarios, gerar_csv_doacoes, gerar_csv_voluntarios
)
from datetime import datetime

def abrir_janela_principal():
    janela = tk.Tk()
    janela.title("Sistema ONG")
    janela.geometry("650x500")

    aba = ttk.Notebook(janela)
    aba.pack(expand=True, fill='both')

    # === Beneficiários ===
    frame_ben = ttk.Frame(aba)
    aba.add(frame_ben, text="Beneficiários")

    tk.Label(frame_ben, text="Nome:").pack()
    nome_entry = tk.Entry(frame_ben)
    nome_entry.pack()

    tk.Label(frame_ben, text="Telefone:").pack()
    tel_entry = tk.Entry(frame_ben)
    tel_entry.pack()

    tk.Label(frame_ben, text="Endereço:").pack()
    end_entry = tk.Entry(frame_ben)
    end_entry.pack()

    tk.Label(frame_ben, text="Documento:").pack()
    doc_entry = tk.Entry(frame_ben)
    doc_entry.pack()

    def salvar():
        adicionar_beneficiario(
            nome_entry.get(), tel_entry.get(), end_entry.get(), doc_entry.get()
        )
        nome_entry.delete(0, tk.END)
        tel_entry.delete(0, tk.END)
        end_entry.delete(0, tk.END)
        doc_entry.delete(0, tk.END)
        atualizar_lista()

    tk.Button(frame_ben, text="Salvar", command=salvar).pack(pady=5)

    lista = ttk.Treeview(frame_ben, columns=("ID", "Nome", "Telefone", "Endereço", "Documento"), show='headings')
    for col in lista["columns"]:
        lista.heading(col, text=col)
    lista.pack(fill=tk.BOTH, expand=True)

    def atualizar_lista():
        for i in lista.get_children():
            lista.delete(i)
        for b in listar_beneficiarios():
            lista.insert('', 'end', values=b)

    def deletar():
        selecionado = lista.selection()
        if selecionado:
            id_sel = lista.item(selecionado, 'values')[0]
            deletar_beneficiario(id_sel)
            atualizar_lista()

    tk.Button(frame_ben, text="Deletar selecionado", command=deletar).pack(pady=5)
    tk.Button(frame_ben, text="Gerar relatório CSV", command=gerar_csv_beneficiarios).pack(pady=5)

    atualizar_lista()

    # === Doações ===
    frame_doa = ttk.Frame(aba)
    aba.add(frame_doa, text="Doações")

    tk.Label(frame_doa, text="ID Beneficiário:").pack()
    ben_id = tk.Entry(frame_doa)
    ben_id.pack()

    tk.Label(frame_doa, text="Item:").pack()
    item = tk.Entry(frame_doa)
    item.pack()

    tk.Label(frame_doa, text="Quantidade:").pack()
    qtd = tk.Entry(frame_doa)
    qtd.pack()

    def salvar_doacao():
        try:
            adicionar_doacao(int(ben_id.get()), item.get(), int(qtd.get()), datetime.now().strftime("%Y-%m-%d"))
            messagebox.showinfo("Salvo", "Doação registrada.")
            ben_id.delete(0, tk.END)
            item.delete(0, tk.END)
            qtd.delete(0, tk.END)
            atualizar_lista_doacoes()
        except:
            messagebox.showerror("Erro", "Verifique os dados.")

    tk.Button(frame_doa, text="Salvar doação", command=salvar_doacao).pack(pady=5)
    tk.Button(frame_doa, text="Gerar relatório CSV", command=gerar_csv_doacoes).pack(pady=5)

    lista_doa = ttk.Treeview(frame_doa, columns=("ID", "Beneficiário", "Item", "Quantidade", "Data"), show='headings')
    for col in lista_doa["columns"]:
        lista_doa.heading(col, text=col)
    lista_doa.pack(fill=tk.BOTH, expand=True)

    def atualizar_lista_doacoes():
        for i in lista_doa.get_children():
            lista_doa.delete(i)
        for d in listar_doacoes():
            lista_doa.insert('', 'end', values=d)

    atualizar_lista_doacoes()

    # === Voluntários ===
    frame_vol = ttk.Frame(aba)
    aba.add(frame_vol, text="Voluntários")

    tk.Label(frame_vol, text="Nome:").pack()
    nome_v = tk.Entry(frame_vol)
    nome_v.pack()

    tk.Label(frame_vol, text="Telefone:").pack()
    tel_v = tk.Entry(frame_vol)
    tel_v.pack()

    tk.Label(frame_vol, text="Área de Atuação:").pack()
    area = tk.Entry(frame_vol)
    area.pack()

    def salvar_voluntario():
        adicionar_voluntario(nome_v.get(), tel_v.get(), area.get())
        nome_v.delete(0, tk.END)
        tel_v.delete(0, tk.END)
        area.delete(0, tk.END)
        atualizar_lista_voluntarios()
        messagebox.showinfo("Salvo", "Voluntário cadastrado.")

    tk.Button(frame_vol, text="Salvar voluntário", command=salvar_voluntario).pack(pady=5)

    lista_vol = ttk.Treeview(frame_vol, columns=("ID", "Nome", "Telefone", "Área de Atuação"), show='headings')
    for col in lista_vol["columns"]:
        lista_vol.heading(col, text=col)
    lista_vol.pack(fill=tk.BOTH, expand=True)

    def atualizar_lista_voluntarios():
        for i in lista_vol.get_children():
            lista_vol.delete(i)
        for v in listar_voluntarios():
            lista_vol.insert('', 'end', values=v)

    tk.Button(frame_vol, text="Gerar relatório CSV", command=gerar_csv_voluntarios).pack(pady=5)
    atualizar_lista_voluntarios()

    janela.mainloop()