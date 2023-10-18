# Função para verificar se um número é par ou ímpar
def verificar_paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Solicita ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Chama a função para verificar a paridade do número
paridade = verificar_paridade(numero)

# Exibe o resultado
print(f"O número {numero} é {paridade}.")
