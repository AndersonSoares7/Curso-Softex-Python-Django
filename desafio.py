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
    forma_retirada = input(f'Qual o Bairro? (1:{bairro_barroco} ou 2:{bairro_saojose})? ')  
    if forma_retirada == '1':
        