'''
Faça um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
- A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
'''


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    alunos = dict()
    alunos['total'] = len(n)
    alunos['maior'] = max(n)
    alunos['menor'] = min(n)
    alunos['média'] = (sum(n)) / len(n)
    if sit:
        if alunos['média'] >= 7:
            alunos['situação'] = 'BOA'
        elif alunos['média'] >= 5:
            alunos['situação'] = 'RAZOÁVEL'
        else:
            alunos['situação'] = 'RUIM'
    return alunos


# Programa principal
resp = notas(4, 4, 6.5, sit=True)
print(resp)
help(notas)
