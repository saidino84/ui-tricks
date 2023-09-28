import tkinter as tk
from tkinter import ttk
from datetime import date

# Criar uma janela principal
root = tk.Tk()
root.title("Treeview com dados por data")
root.geometry("400x300")

# Criar uma Treeview com duas colunas
tree = ttk.Treeview(root, columns=("Produto", "Preço"))
tree.heading("#0", text="Data")
tree.heading("Produto", text="Produto")
tree.heading("Preço", text="Preço")

# Gerar alguns dados de exemplo
dados = [
    (date(2023, 1, 1), "Arroz", 5.00),
    (date(2023, 1, 1), "Feijão", 4.50),
    (date(2023, 1, 2), "Macarrão", 3.00),
    (date(2023, 1, 2), "Molho", 2.50),
    (date(2023, 1, 3), "Carne", 15.00),
    (date(2023, 1, 3), "Salada", 4.00),
]

# Inserir os dados na Treeview, agrupando por data
datas = {} # Dicionário para guardar os itens de data
for data, produto, preco in dados:
    # Verificar se a data já existe na Treeview
    if data not in datas:
        # Criar um novo item de data na Treeview
        datas[data] = tree.insert("", "end", text=data.strftime("%d/%m/%Y"))
    # Inserir o produto e o preço como filho do item de data
    tree.insert(datas[data], "end", values=(produto, f"R$ {preco:.2f}"))

# Empacotar a Treeview na janela
tree.pack(fill="both", expand=True)

# Executar o loop principal da janela
root.mainloop()
