#   IMPORTAR FUNÇÕES DO MODULO FUNCOES
from ProjetosGitHub1.TaskTracker.Funcoes import *




## __________ Inicialização __________  ##

resposta_usuario_operacoes = 0

carregar_dados()

while resposta_usuario_operacoes != 9:
    print("========= BEM VINDO AO MENU DE OPERAÇÕES ==========")
    menu_de_operacoes()
    resposta_usuario_operacoes = int(input("Selecione a opção desejada: "))
    if resposta_usuario_operacoes == 1:
        incluir()

    elif resposta_usuario_operacoes == 2:
        listar()

    elif resposta_usuario_operacoes == 3:
        atualizar()

    elif resposta_usuario_operacoes == 4:
        excluir()

    elif resposta_usuario_operacoes == 9:
        pass

    else:
        print("Digite uma opção válida")



