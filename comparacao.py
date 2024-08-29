num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


iguais = num1 == num2
diferentes = num1 != num2
primeiro_maior = num1 > num2
primeiro_menor = num1 < num2
primeiro_maior_ou_igual = num1 >= num2
primeiro_menor_ou_igual = num1 <= num2


print("Os números digitados são iguais:", iguais)
print("Os números digitados são diferentes:", diferentes)
print("O primeiro número digitado é maior que o segundo:", primeiro_maior)
print("O primeiro número digitado é menor que o segundo:", primeiro_menor)
print("O primeiro número digitado é maior ou igual ao segundo:", primeiro_maior_ou_igual)
print("O primeiro número digitado é menor ou igual ao segundo:", primeiro_menor_ou_igual)