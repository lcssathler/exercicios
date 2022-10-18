from time import sleep
price = float(input('Qual o valor do produto?: '))
print('Nossas formas de pagamento:')
sleep(0.5)
print('\033[31mOpção 1\033[m: \n Á vista/cheque: 10% de desconto. ')
sleep(0.5)
print('\033[31mOpção 2\033[m: \n Á vista no cartão: 5% de desconto.')
sleep(0.5)
print('\033[31mOpcção 3\033[m: \n Em até 2x no cartão: preço normal.')
sleep(0.5)
print('\033[31mOpção 4\033[m: \n 3x ou mais no cartão: 20% de juros.')
sleep(0.5)
print('-=-' * 12)
while True:
    payment = int(input('Qual opção de pagamento você irá escolher?(Utilize apenas números): '))
    print('CALCULANDO...')
    sleep(2)
    if payment == 1:
        discont = 0.1 * price
        print('Você receberá um desconto de R${:.2f}! O preço final será de R${:.2f}.'.format(discont, price - discont))
        break
    elif payment == 2:
        discont = 0.05 * price
        print('Você receberá um desconto de R${:.2f}! O preço final será de R${:.2f}.'.format(discont, price - discont))
        break
    elif payment ==  3:
        print('Seu produto não terá acréscimo de juros ou descontos, logo o preço final será de R${:.2f}.'.format(price))
        break
    elif payment == 4:
        installments = int(input('Em quantas vezes você deseja dividir?: '))
        interest = 0.2 * price
        new_price = float(interest) + float(price)
        print('O juros total será de R${:.2f}. O preço final será de R${:.2f} com {} parcelas de R${:.2f}.'.format(interest, new_price, installments, new_price / installments))
        break
    else:
        print('Digite uma opção válida!')
        sleep(1)
