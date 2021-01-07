def validar_idade(idade):
    if idade < 18:
        print('\nDesculpe, você não tem idade para prosseguir com o processo ', nome)
        return False
    else:
        print('\nPodemos prosseguir com o processo ', nome)
        return True

def escolher_carta():
    print('Selecione uma da opções abaixo para a sua habilitação:')
    print('1-Carro\n2-Moto\n3-Carro e Moto')
    return int(input())

def calcula_preco(escolha):
    valor_carro = 1500
    valor_moto = 1000
    if escolha == 1:
        return valor_carro
    elif escolha == 2:
        return valor_moto
    else:
        return valor_carro + valor_moto

def desconto(valor):
    return valor - (valor * 0.10)

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

if validar_idade(idade):
    escolha = escolher_carta()

    print('\nSuas opções foram selecionadas, o valor será calculado.')
    valor = calcula_preco(escolha)

    print('\n'+nome, ' o valor total é de ', valor, ' reais.')
    print('Mas vamos calcular suas possibilidades de desconto...')
    valor = desconto(valor)

    print('\nCom o seu desconto, seu valor final será de ', valor, ' reais')

    print('Deseja continuar com o processo?\n1-Sim\n2-Não')
    interesse = int(input())
    if interesse == 1:
        print('Perfeito! Suas aulas começarão amanhã!')
    else:
        print('Operação cancelada pelo usuário.\n Você pode reiniciar o processo se mudar de ideia.')