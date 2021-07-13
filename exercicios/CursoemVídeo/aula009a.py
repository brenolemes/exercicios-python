# Manipulando texto

frase = 'Curso em Vídeo Python'

# fatiamento

print(frase[:])
print(frase[0:])
print(frase[:21])
print(frase[10:15])
print(frase[0:15:2])
print(frase[::2])

# Analise

print(frase.count('o'))  # Conta quantos 'o' tem na frase
print(frase.upper().count('O'))  # Coloca a frase em maiuscula e conta quantos 'O' tem na frase
frase = '   Curso em Vídeo Python  ' # Nova variável com espaços no começo e no final frase
print(len(frase)) # Conta quantos elementos tem na frase (incluíndo os espaços do começo e do final)
print(len(frase.strip())) # Conta quantos elemntos tem na frase (excluíndo os espaços do começo e do final)
print('Curso' in frase) # Diz se tem a palavra 'Curso' na frase
print(frase.find('Vídeo')) # Mostra em qual indice começa a palavra 'Vídeo'
print(frase.find('vídeo')) # Como a palavra esta em miniscula o find me retorna -1 (tipo um Falso)
print(frase.lower().find('vídeo')) # Transformando a frase em minuscula pra poder mostrar em qual indice começa a palavra 'vídeo'


# Tranformação

frase = 'Curso em Vídeo Python'
frase = frase.replace('Python', 'Android') # Criando uma variável que tranforma a palavra 'Python' em 'Android'
print(frase)
dividido = frase.split() # Criando uma variável que separa as palavras
print(dividido) # Mostra uma lista
print(dividido[0]) # Mostra o elemento 0 da lista
print(dividido[2][0]) # Mostra o elemento 0 do elemento 2 da lista
# strip, upper, lower fazem parte desse tópico de tranformação
