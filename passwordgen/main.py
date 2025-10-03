import random
import string

print('Bem-vindo ao gerador de senhas')

while True:
    qnt = int(input('Informe o tamanho da senha (8 a 50): '))
    if qnt < 8 or qnt > 50:
        print('Erro: Quantidade fora do limite. Insira um valor correto')
        continue
    else:
        usarl = input('Você quer usar letras minuscúlas? (s/n)').lower() == 's'
        usarn = input('Você quer usar números? (s/n): ').lower() == 's'
        usare = input('Você quer usar carácteres especiais? (s/n): ').lower() == 's'
        usarm = input('Você quer usar letras maiúsculas? (s/n): ').lower() == 's'

    car = ''

    if usarl:
        car += string.ascii_lowercase
    if usarn:
        car += string.digits
    if usare:
        car += string.punctuation
    if usarm:
        car += string.ascii_uppercase

    if not car:
        print('Você precisa escolher pelo menos um tipo de caracter!')
    else:
        senha = "".join(random.choice(car) for _ in range(qnt))
        print('Senha gerada: ', senha)

    cont = input('Você quer gerar outra senha? (s/n): '.lower()) == 's'
    if cont:
        continue
    else:
        print('Obrigado por utilizar nosso gerador!')
        break

