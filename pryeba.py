# edad = 30

# nombre = "Julio"

# concatenado = nombre + " " + str(edad)

# concatenado = f"{nombre} {edad} y soy hetero y macho"

# print(concatenado)
# Realice acá el ejercicio propuesto
def calculadora(*numeros):
    resultado = 0
    for i in numeros:
        resultado += i
    return f"el resultado de la suma {str(numeros).replace(',','+').split("")} es {resultado}"

print(calculadora(5,2,5,6))
