'''
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''


import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print(f'O site pudim não está acessível no momento!')
else:
    print(f'Consegui acessar o site pudim com sucesso!')
    print(site.read())
