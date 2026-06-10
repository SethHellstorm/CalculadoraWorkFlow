from src.calculator import sumar, restar, multiplicar, dividir


def mostrar_menu():
    print("\n===== CALCULADORA =====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("=======================")


def pedir_numeros():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    return a, b


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opción inválida. Intenta de nuevo.")
            continue

        a, b = pedir_numeros()

        try:
            if opcion == "1":
                resultado = sumar(a, b)
                operacion = "+"
            elif opcion == "2":
                resultado = restar(a, b)
                operacion = "-"
            elif opcion == "3":
                resultado = multiplicar(a, b)
                operacion = "*"
            elif opcion == "4":
                resultado = dividir(a, b)
                operacion = "/"

            print(f"\nResultado: {a} {operacion} {b} = {resultado}")
        except ValueError as e:
            print(f"\n{e}")


if __name__ == "__main__":
    main()
    