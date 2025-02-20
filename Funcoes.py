## __________ IMPORTS __________  ##
import json
from _datetime import datetime

## __________ Global __________  ##
lista_todos_os_arquivos = ["NãoIniciadas.json", "EmProgresso.json", "Concluídas.json", "Todas.json"]

## __________ Try __________  ##
def averiguar(funcao, *args):
    try:
        funcao(*args)

    except:
        print("A função não está com o funcionamento correto")

## __________ Pegar a data __________  ##


def data_atualização():
    data_atual = datetime.now().date()
    return data_atual.strftime("%d/%m/%Y")


## __________ Json __________  ##

def salvar_json(lista_qualquer, arquivo):
    with open(arquivo, "w", encoding="utf-8") as arquivo_aberto:
        json.dump(lista_qualquer, arquivo_aberto, ensure_ascii=False)


def ler_json(arquivo):
    with open(arquivo, "r", encoding="utf-8") as arquivo_aberto:
        lista = json.load(arquivo_aberto)
        return lista


## __________ Inicialização __________  ##

def carregar_dados():

    for arquivo in lista_todos_os_arquivos:
        try:
            teste = ler_json(arquivo)
            if teste != []:
                lista = ler_json(arquivo)
            else:
                raise ValueError
        except (ValueError, FileNotFoundError):
            lista = []
            salvar_json(lista, arquivo)


## __________ Menu de operações e opções __________  ##
lista_menu_de_operacoes = ["(1) Incluir", "(2) Listar", "(3) Atualizar", "(4) Excluir",
                               "(9) Voltar ao menu principal"]
def menu_de_operacoes():
    for item in lista_menu_de_operacoes:
        print(item)
    return



lista_menu_de_status = ["(1) Não iniciadas", "(2) Em progresso", "(3) Concluídas", "(4) Todos os arquivos"]

def menu_de_status():
    for item in lista_menu_de_status:
        print(item)


## __________ FUNCIONALIDADES __________  ##

##Incluir
def incluir():

    nome = input("Digite o nome da tarefa: ")
    menu_de_status()
    status = int(input("Digite o status da tarefa: "))
    descricao = input("Descreva a tarefa: ")
    data_atual = str(data_atualização())
    if status == 1:
        arquivo = "NãoIniciadas.json"
        status_transcrito = "Não iniciado"
    elif status == 2:
        arquivo = "EmProgresso.json"
        status_transcrito = "Em Progresso"
    elif status == 3:
        arquivo = "Concluídos.json"
        status_transcrito = "Concluído"
    dicionario = {nome: {"Status": status_transcrito,
                         "Descrição": descricao,
                         "Data da Última modificação": data_atual
                         }}

    lista = ler_json(arquivo)
    lista.append(dicionario)
    salvar_json(lista, arquivo)
    salvar_json(lista, arquivo)
    print("Sua tarefa foi salva com sucesso!")

##Para passar pelos arquivos

def selecao_de_arquivo():
    menu_de_status()


    resp_usuario_status = int(input("Deseja selecionar as tarefas de qual status?"))



    while True:

            try:
                if resp_usuario_status == 1:
                    arquivo = "NãoIniciadas.json"
                    break
                elif resp_usuario_status == 2:
                    arquivo = "EmProgresso.json"
                    break
                elif resp_usuario_status == 3:
                    arquivo = "Concluídas.json"
                    break
                elif resp_usuario_status == 4:
                    arquivo = "Todas.json"
                    break
                else:
                    raise ValueError
            except ValueError:
                print("opção inválida")
                print()
                continue

    return arquivo


##Listar
def listar():
    arquivo = selecao_de_arquivo()
    lista = ler_json(arquivo)
    for item in lista:
        for key, value in item.items():
            print(key)
            print()
            print(value)
            print()
            print()
    return arquivo


##Atualizar
def atualizar():
    arquivo = listar()
    lista = ler_json(arquivo)
    tarefa = input("Digite por extenso a tarefa que deseja alterar: ")

    def complementar(lista, tarefa, novo_valor):
        for item in lista:
            x = item.get(tarefa)
            if x:
                x[chave] = novo_valor
                data_atualização()
                print("O valor foi alterado com sucesso!!!")
                salvar_json(lista, arquivo)

    resp_atualizar = int(input("O que deseja atualizar?"
                               "(1) Status"
                               "(2) Descrição"))
    if resp_atualizar == 1:
        chave = "Status"
        menu_de_status()
        resp = int(input("Em qual status deseja colocar sua tarefa?"))
        if resp == 1:
            novo_valor = "Não iniciada"
        elif resp == 2:
            novo_valor = "Em progresso"
        elif resp == 3:
            novo_valor = "Concluída"
        complementar(lista, tarefa, novo_valor)
    elif resp_atualizar == 2:
        chave = "Descrição"
        novo_valor = input("Digite o novo valor para " + chave + ":")
        complementar(lista, tarefa, novo_valor)


##Excluir
def complementar_excluir_elemento():

    return None


def excluir():
    arquivo =  listar()
    lista = ler_json(arquivo)
    nova_lista = []
    if lista == []:
        print("O grupo de tarefas escolhido está vazio.")
        print("Voltando ao menu principal")
    else:
        tarefa = input("Qual tarefa você deseja excluir?")
        for item in lista:
            for var in list(item.keys()):
                if var == tarefa:
                    del item[tarefa]
        if lista != []:
            for item in lista:
                if item:
                    nova_lista.append(item)
            lista = nova_lista
        elif lista == []:
            lista = []
        salvar_json(lista, arquivo)
        print("Sua tarefa foi excluída com sucesso, jovem!")



























