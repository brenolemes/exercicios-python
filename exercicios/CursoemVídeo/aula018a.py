'''teste = list()  # Criei uma lista chamada teste
teste.append('Breno')   # Adicionei 'Breno' na lista teste
teste.append(21)    # Adicionei '21' na lista teste
galera = list()     # Criei uma lista chamada galera
galera.append(teste[:])    # Adicionei a copia da lista teste dentro da lista galera
teste[0] = 'Maria'  # Troquei 'Breno' por 'Maria' dentro da lista teste (Original)
teste[1] = 27  # Troquei '21' por '27' dentro da lista teste (Original)
galera.append(teste[:])     # Adicionei mais uma copia da lista teste (só que alterada) dentro da lista galera
print(galera)   # Mostrando a lista galera com as COPIAS das listas teste dentro dela

# Ao invés de dar os appends, também pode colocar as listas direto dentro da lista
galera = [['Breno', 21], ['Maria', 21], ['Bruna', 22], ['Pedro', 33]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

# Outra forma de fazer
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))   # Adicionando nomes na copia da lista dado
    dado.append(int(input('idade: ')))  # Adicionando idades na copia da lista dado
    galera.append(dado[:])  # Adicionando dentro da lista galera, copias da lsita dado criadas a cada iteração
    dado.clear()    # É preciso limpar a lsita dado a cada iteração, pois se não o fizer, ira acumulando
print(galera)
totmai = 0
totmen = 0
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maior(es) de idade e {totmen} menor(es) de idade.')

