# Calculadora em Python

print("\n******************* Python Calculator *******************")

value1 = input('Primeiro valor:  ')
value2 = input('Segundo valor: ')
expMath = input('Selecione o tipo de operação (+ - / * ^): ')

if expMath == '+':
    result1 = float(value1) + float(value2)
    print(result1)

elif expMath == '-':
    result2 = float(value1) - float(value2)
    print(result2)

elif expMath == '/':
    result3 = float(value1) / float(value2)
    print(result3)

elif expMath == '*':
    result4 = float(value1) * float(value2)
    print(result4)

elif expMath == '^':
    result5 = float(value1) ** float(value2)
    print(result5)

else:
    print('Operação inválida!')