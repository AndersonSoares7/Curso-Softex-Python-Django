nome_frances = "francês"
nome_doce = "doce"
nome_forma = "forma"

valor_frances = 0.50
valor_doce = 5.00
valor_forma = 5.99

quantidade_frances = 15
quantidade_doce = 20
quantidade_forma = 18

nome_atendente = "Maria"

bairro_barroco = "Barroco"
bairro_saojose = "São José"

frete_barroco = 10.00
frete_saojose = 15.00

codigo_venda = 98568

while True:
    print(f"--Bem vindo(a), Desespero, sou atendente {nome_atendente}")
    escolha = input(f'Temos os pães: {nome_frances}, {nome_doce}, {nome_forma}. Qual você deseja? ')
    if escolha == nome_frances:
        quantidade = int(input("Qual a quantidade? "))
        if quantidade <= quantidade_frances:
            quantidade_frances -= quantidade
            pedido_de_paes = quantidade
            valor_compra = quantidade * valor_frances
            print(f'Seu pedido ficou em R${valor_compra}')
    else:
        print(f'Infelizmente só temos {quantidade_frances} no momento, ')
        break

    forma_retirada = input(f'Qual a forma de retirada? (1: retirar ou 2: entregar)? ')
    if forma_retirada == '2':
       bairro_entrega = input(f"Qual o bairro? (1:{bairro_barroco},2:{bairro_saojose})")
    if bairro_entrega == '1':
        valor_frete = frete_barroco
    if bairro_entrega == '2':
        print('Valor do frete R%{valor_frete}')
    elif bairro_entrega == '2':
        valor_frete = frete_saojose
        print(f'Valor do frete R${valor_frete}')
    else:
        print('Fora da Área de entrega')
        break
    if forma_retirada == '1':
        valor_frete = 0.00
    else:
        break

    dados_cliente = input("Digite seu nome: ")
    forma_pagamento = input('Escolha forma de pagamento (1: dinheiro, 2: cartão): ')

    if forma_pagamento == '1':
        forma_pagamento = 'dinheiro'

    
    else:
        forma_pagamento = 'cartão'

    codigo_venda += 1
        
    print(f'O valor total da sua compra é R${valor_compra + valor_frete}')
    break
