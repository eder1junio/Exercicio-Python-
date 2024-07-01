#Altere as funções pede_nome e pede_telefone de fomar a receberem um parametro opcional.
#Caso esse paramentro seja passado, utilize-o como retorno casa a entrada de dados seja vazia.
import tkinter as tk
import os
from  datetime import datetime
agenda = []
def pede_nome(nome1="nome invalido"):
     nome = input("Nome: ")
     if nome:
         return nome
     else:
        return nome1 

    

def pede_telefone(telefone1 = "telefone invalido"):
    telefone =  input("Telefone: ")
    if telefone:
         return telefone
    else:
        return telefone1 

def mostra_dados(  nome, telefone,indice= None ):
    if indice == None:
        print(f"Nome: {nome} Telefone:{telefone}")

    else:
        print(f"{indice} Nome: {nome} Telefone:{telefone}")

def pede_nome_arquivo():
    return input("Nome do arquivo")

def pesquisa(nome):
    mnome = nome.lower()
    for p , e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p 
    return None

def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])

def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        sn = input("tem certeza que voces gostaria de deleta o nome ")
        if sn.lower() == 's':
            del agenda[p]
        else:
            print("tudo bem !")    
    else:
        print("Nome nao econtrado")

def altera():
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("encontrado")
        mostra_dados(nome,telefone,p)
        nome = pede_nome()
        telefone = pede_telefone()
        sn = input("voce gostaria de realmente altera o arquivo (s/n)")
        if sn.lower() == 's':
            
            agenda[p] = [nome , telefone]
        else:
            print('Tudo bem')    
    else:
        print('Nome nao encontrado.')

def lista():
   # print("\nAgenda\n\n------")
    #for indice, e in enumerate(agenda):
    #    mostra_dados(indice,e[0], e[1] )
    #print("------")
    criaJanela(agenda)

def le(nome_arquivo="teste"):
    global agenda
    if nome_arquivo == "teste":
        nome_arquivo = pede_nome_arquivo()    
    
    with open(nome_arquivo, "r", encoding="utf=8") as arquivo:
        agenda = []
        next(arquivo)
        for l in arquivo.readlines():
            
            nome, telefone = l.strip().split("#")
            agenda.append([nome,telefone])

def grava(data):
    nome_aquivo = pede_nome_arquivo()
    with open (nome_aquivo, "w", encoding="utf=8") as aquivo:
        for indice,e in enumerate(agenda):
            if indice == 0:
                aquivo.write(f"Data da ultima alteração {data}\n")
            aquivo.write(f"{e[0]}#{e[1]}\n")

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <=fim:
                return valor
            else:
                print(f"digite um numero entre os {inicio} e {fim}")
        except ValueError:
            print(f"Valor invalido,favor digitar entre {inicio} e {fim}")
def criaJanela(lista):
    root = tk.Tk()
    root.title("Lista em Ordem Alfabética")
    # Cria uma caixa de listagem (Listbox)
    listbox = tk.Listbox(root)
    listbox.pack(padx=10, pady=10)

    # Adiciona os itens da lista na Listbox
    for item in lista:
        listbox.insert(tk.END, item)

    # Mantém a janela aberta
    root.mainloop()


def menu():
    print("""
          1- Novo
          2 - Altera
          3 - Apaga
          4 - Lista
          5 - Grava
          6 - Lê
          7 - ver tamnho do arquivo 
          8 - Odena lista Por nome 
          0 - Sai
          """)
    return valida_faixa_inteiro("Escolha um opção:", 0 , 8)

def tamanho():
    arquivo = pede_nome_arquivo()
    if os.path.exists(arquivo):
        tamanho = os.path.getsize(arquivo)
        
        return print(f"O tamanho do arquivo e {tamanho} bytes")
    else:
        return print("Nome invalido")

def ordenalista():
    agendaOrgani = sorted(agenda)
    criaJanela(agendaOrgani)

le("eder")       

while True:
    opcao = menu()
    if opcao == 0:
        break
    if opcao == 1:
        novo()
    if opcao == 2:
        altera()
    if opcao == 3:
        apaga()
    if opcao == 4:
        lista()
    if opcao == 5:
    
        data = datetime.now()
        dataCompleta = f"{data.day}/{data.month}/{data.year}"
        grava(dataCompleta)
    if opcao == 6:
        le()
    if opcao == 7:
        tamanho()
    if opcao == 8:
        ordenalista()    
