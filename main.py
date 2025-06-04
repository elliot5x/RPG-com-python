from time import sleep
from sys import exit
from os import system, name
import random

inventario = []
classe_do_personagem = []
opcoes_do_jogador = []

def cls():
    system('cls') if name == 'nt' else system('clear')
cls()

def menu():
    while True:
        try:
            cls()
            print("==== RPG ====\n")
            print("[1] Jogar\n[2] Sair\n")
            digite = int(input(">> "))

            opcoes = {
                1: classe,
                2: exit
            }

            if digite in opcoes:
                opcoes[digite]()
            else:
                print("Erro: escolhas apenas números válidos")
                sleep(1.5)
                cls()
        except ValueError:
            print("Erro: Digite apenas números.")
            sleep(1.5)
            cls()
def classe():
    while True:
        try:
            cls()
            print("Escolha um personagem:\n")
            print("[1] Ladrão\n[2] Mago\n")
            digite = int(input(">> "))

            if digite == 1:
                classe_do_personagem.append("Ladrão")
                jogar()
            elif digite == 2:
                classe_do_personagem.append("Mago")
                jogar()
            else:
                print("Erro")
                sleep(1.5)
                cls()
        except ValueError:
            print("Erro")
            sleep(1.5)
            cls()

def jogar():
    while True:
        try:
            cls()
            print("Você esta preso em uma cela.\n")
            print("[1] Olhar em volta\n[2] Abrir cela")
            digite = int(input(">> "))

            if digite == 1:
                cls()
                print("Tem apenas uma cama suja do seu lado\n")
                opcoes_do_jogador.append("vasculhar")

                if "vasculhar" in opcoes_do_jogador:
                    print("[1] Vasculhar cama\n[2] Voltar")
                    vasculhando = int(input(">> "))

                    if vasculhando == 1:
                        if "grampo" in inventario:
                            print("A cama esta vazia")
                            sleep(2)
                            cls()
                        else:
                            print("Você achou um grampo velho\n")
                            input("Aperte ENTER para continuar.")
                            inventario.append("grampo")
                    elif vasculhando == 2:
                        jogar()
                        
                else:
                    print("Escolha uma das opções")

            elif digite == 2:
                if "grampo" in inventario:
                    print("*você usou o grampo\n")
                    inventario.clear()
                    print("Você está livre.")
                    input("")
                    menu()
                else:
                    print("A cela está trancada")
                    sleep(2)
                    cls()
            else:
                print("Escolha um dos números")
                sleep(2)
                cls()
        except ValueError:
            print("Escolha apenas números válidos.")
            sleep(2)
            cls()
    
menu()