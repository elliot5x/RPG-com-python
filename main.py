from time import sleep
from os import system, name
from sys import exit
import random

def cls():
    system("cls") if name == 'nt' else system("clear")
cls()

porcentagem_dificl = 70

itens = {
    "gaveta": ["documento"],
    "gaveta trancada": ["chave do bau"],
    "bau": ["chave da porta"],
    "cama": ["grampo velho", "grampo velho", "grampo velho", "chave da gaveta"] 
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
            if "documento" in mente:
                    cls()
                    print("[1] Investigar cama\n[2] Olha em baixo da cama\n[3] voltar")
                    escolher = int(input(">> "))
                    if escolher == 1:
                        investigar()
                    elif escolher == 2:
                        if "chave da gaveta" in inventario:
                            print("Esse lugar esta vazio.")
                            input("\nENTER para continuar")
                            inicio()
                        else:
                            print("Você achou a chave da gaveta.")
                            print("*Chave da gaveta foi adicionada ao inventario.")
                            inventario.append("chave da gaveta")
                            itens["cama"].remove("chave da gaveta")
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
                if "documento" in mente:
                    print("Gaveta vazia")
                    input("\nENTER para continuar")
                else:
                    print("Você achou um documento que diz:\nOlhe em baixo da cama")
                    mente.append("documento")
                    itens["gaveta"].remove("documento")
                    input("\nENTER para continuar")
            elif escolha == 2:
                if "chave da gaveta" in inventario:
                    print("*Você abriu a gaveta\n")
                    print("Tem uma chave aqui\n")
                    print("*Chave do bau foi adicionada ao inventario e gaveta foi trancada novamente.")
                    inventario.append("chave do bau")
                    itens["gaveta trancada"].remove("chave do bau")
                    inventario.remove("chave da gaveta")
                    mesa()
                    input("\nENTER para continuar")
                elif "grampo velho" in inventario:
                        random.random() < (porcentagem_dificl / 100.0)
                        print("*O grampo quebrou\n")
                        inventario.remove("grampo velho")
                        input("\nENTER para continuar")
                elif "grampo velho" in inventario and "chave da gaveta" in inventario:
                    print("*Você abriu a gaveta\n")
                    print("Tem uma chave aqui\n")
                    print("*Chave do bau foi adicionada ao inventario e gaveta foi trancada novamente.")
                    inventario.append("chave do bau")
                    itens["gaveta trancada"].remove("chave do bau")
                    inventario.remove("chave da gaveta")
                    mesa()
                    input("\nENTER para continuar")
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
            if "grampo velho" in inventario:
                print("Você só pode carregar um grampo por vez")
                input("\nENTER para continuar")
                cama()
            elif "grampo velho" not in itens["cama"]:
                print("Acabou os grampos. :(")
                input("\nENTER para continuar")
                cama()
                
            else:
                print("Você achou um grampo velho\n")
                print("*Grampo velho foi enviado ao inventario")
                inventario.append("grampo velho")
                itens["cama"].remove("grampo velho")
                input("\nENTER para continuar")
                cama()
        except ValueError:
            print("Erro: Escolha um número válido.")
            input("\nENTER para continuar")

def bau():
    while True:
        try:
            if "chave do bau" in inventario:
                print("abrindo bau com a chave")
                sleep(2)
                for i in range(0,1):
                    cls()
                    print("Destrancando bau.")
                    sleep(0.5)
                    cls()
                    print("Destrancando o bau..")
                    sleep(0.5)
                    cls()
                    print("Destrancando o bau...")
                    sleep(0.5)
                    cls()
                    input("*Bau aberto")
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
    print("Obrigado por jogar :)\n")
    input("\nENTER para continuar")
    menu()
menu()