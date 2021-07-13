'''
a - Vamos criar um menu em Python, usando modularização.
b - Vamos ver como fazer acesso a arquivos usando o Python.
c - Vamos finalizar o projeto de acesso a arquivos em Python.
'''
from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o cionteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input(f'Nome: ')).strip()
        idade = leiaInt(f'Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu
        print(f'\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
