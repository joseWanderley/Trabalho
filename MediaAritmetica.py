m = int(input('Digite um número inteiro m: '))
n = int(input('Digite um número inteiro n: '))


soma = m + n
media = soma/2

if(media >= 6){
  print("Média maior ou igual 6.")
}else{
  print("Média menor que 6.")
}

rad = m**0.5

print(rad)

print('A média aritmética entre ' + str(m) + ' e '+ str(n) + ' é '+ str(media) + '.')
