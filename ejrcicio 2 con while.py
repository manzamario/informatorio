texto = input("Ingrese un texto: ")

# Ciclo while para permitir que el usuario ingrese varias veces diferentes conjuntos de letras
while True:
    # Solicitar al usuario que ingrese tres letras a buscar, separadas por comas
    letras = input("Ingrese tres letras a buscar, separadas por comas (o 'salir' para terminar): ")

    # Verificar si el usuario desea salir del ciclo while
    if letras.lower() == 'salir':
        print("¡Hasta luego!")
        break

    # Convertir las letras ingresadas a minúsculas y crear una lista con ellas
    letras = letras.lower().split(",")

    # Cantidad de veces que aparece cada letra
    for letra in letras:
        cantidad = texto.lower().count(letra)
        print(f"La letra {letra} aparece {cantidad} veces en el texto.")

    # Cantidad total de palabras
    palabras = texto.split()
    cantidad_palabras = len(palabras)
    print(f"La cantidad total de palabras en el texto es: {cantidad_palabras}.")

    # Primera letra y última letra
    primera_letra = texto[0]
    ultima_letra = texto[-1]
    print(f"La primera letra es: {primera_letra} y la última letra es: {ultima_letra}.")

    # Texto en orden inverso
    texto_inverso = texto[::-1]
    print(f"El texto en orden inverso es: {texto_inverso}.")

    # Si la palabra "python" aparece en el texto
    if "python" in texto.lower():
        print("La palabra 'python' aparece en el texto.")
    else:
        print("La palabra 'python' no aparece en el texto.")
