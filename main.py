from time import sleep
from os import system, name
from sys import exit
import random

def cls():
    system("cls") if name == 'nt' else system("clear")
cls()

opcoes_do_jogador = {
    "inventario": [],
    "classe_do_personagem": []
}

# Sistema de lockpicking
lockpick = {
    "facil": ["open", "lock", "lock"],
    "medio": ["open", "lock", "lock", "lock", "lock"],
    "dificil": ["open", "lock", "lock", "lock", "lock", "lock", "lock"]
}
porcentagem_facil = 10
porcentagem_medio = 40
porcentagem_dificl = 60

def menu():
    while True:
        try:
            cls()
            print("=== MENU ===\n")
            print("*Digitar 00 em qualquer momento volta para o menu*\n")
            print("[1] Jogar\n[2] Sair\n")
            escolha = int(input(">> "))

            opcoes = {
                1: inicio,
                2: exit
            }
            if escolha in opcoes:
                opcoes_do_jogador["inventario"].clear()
                opcoes[escolha]()
            else:
                print("Erro: Escolha um número válido.")
                sleep(1.5)

        except ValueError:
            print("Erro: Escolha apenas números válidos.")
            sleep(1.5)

def inicio():
    while True:
        try:
            cls()
            print("=== A CELA ===\n")
            print("*você está em uma cela\n")
            print("[1] Olhar em volta\n[2] Tentar abrir a cela\n[3] Gritar que é inocente\n[4] Encostar na grade\n")
            digite = int(input(">> "))

            gritar = ["Parece que ninguem ouviu", "AAAAAAAAAAA", "EU SOU INOCENTEEEEE", "GUARDA: CALA A BOCA"]

            if digite == 1:
                olhando()
            elif digite == 2:
                if "grampo" in opcoes_do_jogador["inventario"]:
                    lock = random.choice(lockpick["facil"])

                    if lock == "open":
                        saindo_da_cela()
                    else:
                        print("Mais que porcaria")
                        if random.random() < (porcentagem_facil / 100.0):
                            opcoes_do_jogador["inventario"].remove("grampo")
                        print("*O seu grampo quebrou")
                        input("\nEnter para continuar")

                else:
                    print("A cela está trancada")
                    sleep(2)
            elif digite == 3:
                print(random.choice(gritar))
                sleep(2)
            elif digite == 4:
                print("Você encosta na grade e observa os presos e alguns guardas ao longe\n")
                input("ENTER para voltar")
            elif digite == 00:
                menu()
            else:
                print("Erro: escolha um número válido.")
                sleep(1.5)
        except ValueError:
            print("Erro: Escolha apenas números válidos.")
            sleep(1.5)

def olhando():
    while True:
        try:
            cls()
            print("=== A CELA ===\n")
            print("Tem uma cama velha e um colega de cela\n")
            print("[1] Ver a cama velha\n[2] Falar com o preso\n[3] Voltar")
            escolha = int(input(">> "))

            if escolha == 1:
                if "grampo" in opcoes_do_jogador["inventario"]:
                    print("A cama está vazia")
                    sleep(1.5)
                else:
                    print("*Você pegou o grampo\n")
                    opcoes_do_jogador["inventario"].append("grampo")
                    sleep(1.5)
            elif escolha == 2:
                preso_john()
            elif escolha == 3:
                inicio()
            elif escolha == 00:
                menu()
            else:
                print("Erro: Escolha um número válido.")
                sleep(1.5)

        except ValueError:
            print("Erro: Escolha apenas números válidos.")
            sleep(1.5)

def preso_john():
    while True:
        try:
            cls()
            print("=== JOHN O PRESO ===\n")
            print("O que você quer garoto?")
            print("[1] ... [2] ... [3] Voltar")
            escolha = int(input(">> "))

            if escolha == 1:
                print("...")
                sleep(1.5)
            elif escolha == 2:
                print("...")
                sleep(1.5)
            elif escolha == 3:
                olhando()
            elif escolha == 00:
                menu()
            else:
                print("Erro: Escolha um número válido.")
                sleep(1.5)

        except ValueError:
            print("Erro: Escolha apenas números válidos.")
            sleep(1.5)

def saindo_da_cela():
    cls()
    print("*Você saiu da cela.")
    input(" Aperte ENTER para sair")
    menu()

menu()