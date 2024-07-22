"""Este programa genera una contraseña segura de forma aleatoria y 
opcionalmente puedes incluir una palabra clave"""
import random
import string

def generar_contraseña(longitud, palabra_clave=None):
    caracteres = string.ascii_letters + string.digits + string.punctuation

    contraseña_aleatoria = ''.join(random.choice(caracteres) for _ in range(longitud))

    if palabra_clave:
        longitud_aleatoria = longitud - len(palabra_clave)
        if longitud_aleatoria <= 0:
            print("La longitud de la palabra clave es mayor o igual a la longitud de la contraseña.")
            return None

        
        contraseña_aleatoria = ''.join(random.choice(caracteres) for _ in range(longitud_aleatoria))

        
        posicion_insercion = random.randint(0, len(contraseña_aleatoria))
        contraseña = contraseña_aleatoria[:posicion_insercion] + palabra_clave + contraseña_aleatoria[posicion_insercion:]
    else:
        contraseña = contraseña_aleatoria

    return contraseña

def main():
    longitud = int(input("Ingrese la longitud deseada de la contraseña: "))
    palabra_clave = input("Ingrese una palabra clave (opcional): ")

    contraseña = generar_contraseña(longitud, palabra_clave)

    if contraseña:
        print("Tu contraseña segura es:", contraseña)
    else:
        print("No se pudo generar la contraseña. Por favor, intenta nuevamente con una longitud válida.")

if __name__ == "__main__":
    main()
