try:
	numero = int(input("Digite um número: "))
	print(f"Você digitou um número inteiro! {numero}")
except ValueError:
	print("Oh my friend, esse não é um numero inteiro, tenta de novo please!")


idade = int(input("digite a sua idade: "))

if idade < 12:
    print("Você é uma criança.")
elif 12 <= idade <= 17:
    print("Você é um adolescente.")
elif 18 <= idade <= 59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")
    



