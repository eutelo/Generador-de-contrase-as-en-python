# Generador de contraseñas en Python
import string
import secrets

# ============================================
# Función auxiliar: preguntar s/n
# ============================================
def preguntar_sn(titulo):
    while True:
        print("================================")
        print(titulo)
        print("================================")
        print('Responde "s" para sí o "n" para no.\n')

        respuesta = input("(s/n): ").strip().lower()

        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False

        # Mensaje de error mixto B + C + separación visual
        print("\n---------------------------")
        print("Entrada inválida")
        print("---------------------------")
        print('Ups, esa opción no es válida.')
        print('Por favor escribe "s" o "n".\n')


# ============================================
# Función: pedir opciones al usuario
# ============================================
def pedir_opciones():
    opciones_longitud = [8, 12, 16, 20, 24]

    # Selección de longitud
    while True:
        print("================================")
        print("Selección de longitud")
        print("================================\n")

        print("1) 8 caracteres")
        print("2) 12 caracteres")
        print("3) 16 caracteres")
        print("4) 20 caracteres")
        print("5) 24 caracteres\n")

        opcion = input("Elige una opción (1-5): ").strip()

        if opcion in ["1", "2", "3", "4", "5"]:
            longitud = opciones_longitud[int(opcion) - 1]
            break

        # Mensaje de error mixto B + C
        print("\n---------------------------")
        print("Entrada inválida")
        print("---------------------------")
        print("Ups, esa opción no es válida.")
        print("Por favor elige un número del 1 al 5.\n")

    # Preguntas de complejidad
    usar_minusculas = preguntar_sn("Incluir minúsculas")
    usar_mayusculas = preguntar_sn("Incluir mayúsculas")
    usar_numeros    = preguntar_sn("Incluir números")
    usar_simbolos   = preguntar_sn("Incluir símbolos")

    # Validación mixta
    if not (usar_minusculas or usar_mayusculas or usar_numeros or usar_simbolos):
        print("\n---------------------------")
        print("Ajuste automático")
        print("---------------------------")
        print("Parece que no seleccionaste ningún tipo de carácter.")
        print("Activaré minúsculas automáticamente para que la contraseña sea válida.\n")
        usar_minusculas = True

    return {
        "longitud": longitud,
        "usar_minusculas": usar_minusculas,
        "usar_mayusculas": usar_mayusculas,
        "usar_numeros": usar_numeros,
        "usar_simbolos": usar_simbolos
    }


# ============================================
# Función: generar contraseña segura
# ============================================
def generar_password(opciones):
    longitud = opciones["longitud"]

    usar_minusculas = opciones["usar_minusculas"]
    usar_mayusculas = opciones["usar_mayusculas"]
    usar_numeros    = opciones["usar_numeros"]
    usar_simbolos   = opciones["usar_simbolos"]

    pool = ""

    if usar_minusculas:
        pool += string.ascii_lowercase
    if usar_mayusculas:
        pool += string.ascii_uppercase
    if usar_numeros:
        pool += string.digits
    if usar_simbolos:
        pool += string.punctuation

    password_chars = []

    # Garantizar al menos un carácter de cada tipo activado
    if usar_minusculas:
        password_chars.append(secrets.choice(string.ascii_lowercase))
    if usar_mayusculas:
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if usar_numeros:
        password_chars.append(secrets.choice(string.digits))
    if usar_simbolos:
        password_chars.append(secrets.choice(string.punctuation))

    # Rellenar el resto
    while len(password_chars) < longitud:
        password_chars.append(secrets.choice(pool))

    # Mezclar para evitar patrones
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


# ============================================
# Programa principal
# ============================================
def main():
    print("================================")
    print("Generador de contraseñas")
    print("================================")
    print("Crea contraseñas seguras fácilmente.\n")

    while True:
        opciones = pedir_opciones()
        password = generar_password(opciones)

        print("================================")
        print("Contraseña generada")
        print("================================\n")

        print(f">>> {password} <<<\n")
        print("Guárdala en un lugar seguro.\n")

        print("================================")
        print("¿Deseas generar otra contraseña?")
        print("================================")
        print("Puedes generar tantas como quieras.\n")

        otra = input("(s/n): ").strip().lower()

        while otra not in ["s", "n"]:
            print("\n---------------------------")
            print("Entrada inválida")
            print("---------------------------")
            print('Ups, esa opción no es válida.')
            print('Por favor escribe "s" o "n".\n')
            otra = input("(s/n): ").strip().lower()

        if otra == "n":
            print("\nGracias por usar el generador de contraseñas. ¡Hasta luego!\n")
            break


# ============================================
# Punto de entrada
# ============================================
if __name__ == "__main__":
    main()
