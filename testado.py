import random
from time import sleep
from os import system, name
from sys import exit

def cls():
    system("cls") if name == 'nt' else system("clear")
cls()


opcoes_jogo = {
    "invetario":[]
}

itens_do_jogo = ["chave"]


porcentagem_facil = 20
porcentagem_dificil = 60

# GAMEPLAY
def jogo():
     while True:
          try:
            cls()
            print("Pegar a chave do bau ou abri o bau.\n")
            print("[1] Bau\n[2]Chave\n")
            escolha = int(input(">> "))

            if escolha == 1:
                if "chave" in opcoes_jogo["invetario"]:
                    cls()
                    print("tentando abrir")
                    input("\nENTER para continuar")
                    if random.random() < (porcentagem_facil / 100.0):
                        cls()
                        print("A chave quebrou\n")
                        input("\nENTER para continuar.")
                        opcoes_jogo["invetario"].remove("chave")
                    else:
                        cls()
                        print("== Bau aberto ==\n")
                        print("Tem nada no bau")
                        input("\nENTER para continuar.")
                else:
                    cls()
                    print("O bau esta trancado")
                    input("\nENTER para continuar")
            elif escolha == 2:
                if "chave" in opcoes_jogo["invetario"]:
                    cls()
                    print("Você ja tem a chave")
                    input("\nENTER para sair")
                else:
                    if "chave" in itens_do_jogo:
                        cls()
                        print("Você pegou uma chave")
                        opcoes_jogo["invetario"].append(itens_do_jogo[0])
                        itens_do_jogo.clear()
                        input("\nENTER para sair")
                    else:
                        print("Esse Lugar está vazio")
                        input("\nENTER para sair")
            else:
                print("Erro")
                sleep(1.5)


          except ValueError:
              print("ERRO")
              sleep(1.5)
jogo()