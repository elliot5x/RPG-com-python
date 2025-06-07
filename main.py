from time import sleep
from os import system, name
from sys import exit
import random
import uuid

def cls():
    system("cls") if name == 'nt' else system("clear")
cls()

chande_de_quebrar = 90 # São 90% de chance de quebrar.

itens_disponiveis = {
    "gaveta": {
        "nome": "Documento Confidencial",
        "quantidade": 1,
        "descricao": "Tente olhar de baixo da cama"
    },
    "gaveta_trancada": {
        "nome": "Chave do Bau",
        "quantidade": 1,
        "descricao": "Pode ser usada para abrir o bau."
    },
    "cama": {
        "grampo": {
            "nome": "Grampo Velho",
            "quantidade": 3,
            "descricao": "Pode ser usado para abrir qualquer tranca, mas quebra com muita facilidade."
        },
        "chave": {
            "nome": "Chave da Gaveta",
            "quantidade": 1,
            "descricao": "Pode ser usada para abrir a gaveta trancada."
        }
    }
}

inventario = []
mente = []


def menu():
    while True:
        try:
            cls()
            print("=== MENU ===\n")
            print("++ digitar 00 volta ao menu ++\n")
            print("[1] Jogar\n[2] Sair\n")
            digite = int(input(">> "))

            opcoes = {
                1: inicio,
                2: exit
            }

            if digite in opcoes:
                opcoes[digite]()
            else:
                print("Erro: Número inválido.")
                input("\nENTER para continuar")
        except ValueError:
            print("Erro: Escolha um número válido.")
            input("\nENTER para continuar")

def inicio():
    while True:
        try:
            cls()
            print("Tem uma mesa, uma cama e um bau em frente a cama\n")
            print("[1] Ver cama\n[2] Ver a mesa\n[3] Ver o bau\n")
            digitar = int(input(">> "))
            opcoes = {
                1: cama,
                2: mesa,
                3: bau,
                00: menu
            }
            if digitar in opcoes:
                opcoes[digitar]()
            else:
                print("Erro: número inválido")
                input("\nENTER para continuar")
        except ValueError:
            print("Erro: Escolha um número válido.")
            input("\nENTER para continuar")
def cama():
    while True:
        try:
            cls()
            print("=== CAMA ===\n")
            if "Documento Confidencial" in mente:
                    cls()
                    print("[1] Investigar cama\n[2] Olha em baixo da cama\n[3] voltar")
                    escolher = int(input(">> "))
                    if escolher == 1:
                        investigar()
                    elif escolher == 2:
                        if "Chave da Gaveta" in inventario:
                            print("Esse lugar esta vazio.")
                            input("\nENTER para continuar")
                            cama()
                        else:
                            print(f"Você achou a {itens_disponiveis['cama']["chave"]["nome"]}")
                            print(f"*{itens_disponiveis['cama']["chave"]["nome"]} foi adicionada ao inventario.")
                            inventario.append("Chave da Gaveta")
                            sua_quantidade = itens_disponiveis["cama"]["chave"]["quantidade"]
                            itens_disponiveis["cama"]["chave"]["quantidade"] -= sua_quantidade
                            input("\nENTER para continuar")
                            cama()
                    elif escolher == 3:
                        inicio()
                    elif escolher == 00:
                        menu()
                    else:
                        print("Erro: Escolha um número válido.")
            else:
                cls()
                print("[1] Investigar cama\n[2] voltar")
                escolha = int(input(">> "))

                if escolha == 1:
                    investigar()
                elif escolha == 2:
                    inicio()
                elif escolha == 00:
                    menu()
                else:
                    print("Erro: Escolha um número válido.")
                    input("\nENTER para continuar")

        except ValueError:
            print("Erro: Escolha um número válido.")
            input("\nENTER para continuar")

def mesa():
    while True:
        try:
            cls()
            print("== MESA ==\n")
            print("Tem duas Gavetas aqui")
            print("[1] Abrir gaveta de cima\n[2] Abrir gaveta de baixo\n[3] Voltar\n")
            escolha = int(input(">> "))
    
            if escolha == 1:
                if "Documento Confidencial" in mente:
                    print("Gaveta vazia")
                    input("\nENTER para continuar")
                else:
                    print(f"Você achou o {itens_disponiveis['gaveta']["nome"]} que diz:\n{itens_disponiveis['gaveta']["descricao"]}")
                    mente.append("Documento Confidencial")
                    sua_quantidade = itens_disponiveis["gaveta"]["quantidade"]
                    itens_disponiveis["gaveta"]["quantidade"] -= sua_quantidade
                    input("\nENTER para continuar")
            elif escolha == 2:
                if "Chave da Gaveta" in inventario:
                    cls()
                    print("*Você abriu a gaveta\n")
                    print("Tem uma chave aqui\n")
                    print(f"*{itens_disponiveis['gaveta_trancada']["nome"]} foi adicionada ao inventario e gaveta foi trancada novamente.")
                    input("\nENTER para continuar")
                    inventario.append("Chave do Bau")
                    quantidade_chave_bau = itens_disponiveis["gaveta_trancada"]["quantidade"]
                    itens_disponiveis["gaveta_trancada"]["quantidade"] -= quantidade_chave_bau
                    mesa()
                    
                elif "Grampo Velho" in inventario:
                        print("Você tenta abrir a gaveta com um grampo...")
                        input("\nENTER para continuar")
                        if random.random() < (chande_de_quebrar / 100.0):
                            print("*O grampo quebrou\n")
                            inventario.remove("Grampo Velho")
                            input("\nENTER para continuar")
                        else:
                            cls()
                            print("*Você conseguiu abrir a gaveta!\n")
                            input("\nENTER para continuar")
                            inventario.remove("Grampo Velho")
                            if itens_disponiveis["gaveta_trancada"]["quantidade"] > 0:
                                cls()
                                print("Tem uma chave aqui.\n")
                                print(f"*{itens_disponiveis['gaveta_trancada']['nome']} foi adicionada ao inventario.")
                                input("\nENTER para continuar")
                                inventario.append("Chave do Bau")
                                itens_disponiveis["gaveta_trancada"]["quantidade"] -= 1
                            else:
                                cls()
                                print("A gaveta está vazia.")
                                input("\nENTER para continuar")
                            mesa()
                else:
                    print("A gaveta esta trancada.")
                    input("\nENTER para continuar")
            elif escolha == 3:
                inicio()
            elif escolha == 00:
                menu()
        except ValueError:
            print("Erro: Escolha um número válido.")
            input("\nENTER para continuar") 

def investigar():
    while True:
        try:
            if "Grampo Velho" in inventario:
                print("Você só pode usar um grampo por vez.\n")
                print(f"restam {itens_disponiveis["cama"]["grampo"]["quantidade"]} grampos.")
                input("\nENTER para continuar")
                cama()  
            else:
                if itens_disponiveis["cama"]["grampo"]["quantidade"] > 0:
                    print("Você achou um grampo velho\n")
                    print(f"*{itens_disponiveis['cama']["grampo"]["nome"]} foi enviado ao inventario")
                    inventario.append("Grampo Velho") 
                    itens_disponiveis["cama"]["grampo"]["quantidade"] -= 1
                    input("\nENTER para continuar")
                    cama()
                else:
                    print("Esse Lugar esta Vazio.")
                    input("\nENTER para continuar")
                    cama()
        except ValueError:
            print("Erro: Escolha um número válido.")
            input("\nENTER para continuar")

def bau():
    while True:
        try:
            if "Chave do Bau" in inventario:
                print("abrindo bau com a chave\n")
                input("\nENTER para continuar")
                cls()
                print("O bau foi aberto e tinha muitos tesouros.\n")
                input("\nENTER para continuar")
                saida()
            elif "Grampo Velho" in inventario:
                print("Você tenta abrir o bau com um grampo velho...")
                input("\nENTER para continuar")
                if random.random() < (chande_de_quebrar / 100.0):
                    print("*O grampo quebrou\n")
                    inventario.remove("Grampo Velho")
                    input("\nENTER para continuar")
                    inicio()
                else:
                    cls()
                    print("Você conseguiu abrir o bau!")
                    input("\nENTER para continuar")
                    cls()
                    print("O bau foi aberto e tinha muitos tesouros.\n")
                    input("\nENTER para continuar")
                    saida() 
            else:
                print("O bau esta trancado")
                input("\nENTER para continuar") 
                inicio()        
        except ValueError:
            print("Erro: Escolha um número válido.")
            input("\nENTER para continuar")

def saida():
    cls()
    print("Obrigado por jogar :)\n")
    inventario.clear()
    itens_disponiveis.clear()
    mente.clear()
    input("\nENTER para continuar")
    menu()
menu()