#4 - Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor. 
# As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. 
# A saída deve estar formatada exatamente como indicado.

valor = int (input("Digite o valor :")) 
notas_100 = valor // 100
valor = valor % 100 
notas_50 = valor // 50
valor = valor % 50
notas_20 = valor // 20
valor = valor % 20
notas_10 = valor // 10
valor = valor % 10
notas_5 = valor // 5
valor = valor % 5
moedas_1 = valor // 1
valor = valor % 1
print (f"{notas_100} nota(s) de 100")
print (f"{notas_50} nota(s) de 50")
print (f"{notas_20} nota(s) de 20")
print (f"{notas_10} nota(s) de 10")
print (f"{notas_5} nota(s) de 5")
print (f"{moedas_1} moeda(s) de 1")