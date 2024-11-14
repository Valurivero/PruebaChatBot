diccionario = {}
print("vamos a crear tu diccionario. Introducí `salir`cuando finalices") 
while True:
    clave = input("Ingrese una clave, por ejemplo un nombre:")
    if clave.lower() == 'salir': 
        break


    
print(diccionario)
for clave, valor in Diccionario.items():
    print(f"{clave} {valor}")

print(Diccionario.get(clave))