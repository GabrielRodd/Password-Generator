import random
import string

#Função que cria os caracteres possíveis da senha
def password_generator(first_caracter: str, size_pass=8, ):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    password_user = first_caracter.upper() + ""

#Loop que itera sobre cada caracter, definindo-o de forma aleatória
    for digit in range(size_pass):
        digit = random.choice(options)
        password_user += digit

    return password_user


choice_user = int(input('Digite o numero de caracteres desejados para a senha:'))
first_caracter = input('Digite qual quer que seja o primeiro caracter:')
password = password_generator(first_caracter, choice_user)


print(f'Senha gerada:{password}')