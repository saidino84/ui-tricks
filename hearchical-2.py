import tkinter as tk
from tkinter import ttk
from datetime import date, timedelta
import random

# Criar uma janela principal
root = tk.Tk()
root.title("Treeview com mais dados e colunas")
root.geometry("600x400")

# Criar um frame para conter a Treeview e as barras de rolagem
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Criar uma Treeview com cinco colunas
tree = ttk.Treeview(frame, columns=("Código", "Produto", "Custo", "Venda", "Proveniência"))
tree.heading("#0", text="Data")
tree.heading("Código", text="Código")
tree.heading("Produto", text="Produto")
tree.heading("Custo", text="Custo")
tree.heading("Venda", text="Venda")
tree.heading("Proveniência", text="Proveniência")


tree.column("Código", width=100)
tree.column("Produto", width=100)
tree.column("Custo", width=100)
tree.column("Venda", width=100)
tree.column("Proveniência", width=100)

# Gerar alguns dados de exemplo
produtos = ["Arroz", "Feijão", "Macarrão", "Molho", "Carne", "Salada", "Pão", "Queijo", "Leite", "Café"]
proveniências = ["Brasil", "Argentina", "Itália", "China", "EUA", "França", "Portugal", "Alemanha", "Japão", "Moçambique"]
dados = []
data_inicial = date(2023, 1, 1)
for i in range(60):
    # Gerar uma data aleatória entre 01/01/2023 e 31/03/2023
    data = data_inicial + timedelta(days=random.randint(0, 89))
    # Gerar um produto aleatório da lista de produtos
    produto = random.choice(produtos)
    # Gerar um código aleatório de 4 dígitos
    codigo = random.randint(1000, 9999)
    # Gerar um custo aleatório entre 1 e 20 reais
    custo = random.uniform(1, 20)
    # Gerar um preço de venda aleatório entre o custo e o custo + 10 reais
    venda = random.uniform(custo, custo + 10)
    # Gerar uma proveniência aleatória da lista de proveniências
    proveniência = random.choice(proveniências)
    # Adicionar os dados à lista de dados
    dados.append((data, codigo, produto, custo, venda, proveniência))

# Inserir os dados na Treeview, agrupando por data
datas = {} # Dicionário para guardar os itens de data
for data, codigo, produto, custo, venda, proveniência in dados:
    # Verificar se a data já existe na Treeview
    if data not in datas:
        # Criar um novo item de data na Treeview
        datas[data] = tree.insert("", "end", text=data.strftime("%d/%m/%Y"))
    # Inserir o código, o produto, o custo, a venda e a proveniência como filho do item de data
    tree.insert(datas[data], "end", values=(codigo, produto, f"R$ {custo:.2f}", f"R$ {venda:.2f}", proveniência))

# Criar uma barra de rolagem vertical para a Treeview
scroll_y = tk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll_y.pack(side="right", fill="y")
tree.configure(yscrollcommand=scroll_y.set)

# Criar uma barra de rolagem horizontal para a Treeview
scroll_x = tk.Scrollbar(frame, orient="horizontal", command=tree.xview)
scroll_x.pack(side="bottom", fill="x")
tree.configure(xscrollcommand=scroll_x.set)

# Empacotar a Treeview no frame
tree.pack(fill="both", expand=True)

# Executar o loop principal da janela
root.mainloop()
