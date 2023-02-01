"""
Crie um programa usando matemática e f-Strings que nos diga quantos dias,
semanas, meses nos restam se vivermos até os 90 anos de idade.
Ele levará sua idade atual como entrada e emitirá uma mensagem
com nosso tempo restante neste formato:
Você tem x dias, y semanas e z meses restantes.
Onde x, ye z são substituídos pelos números calculados reais.
"""
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining  * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)
