<<<<<<< HEAD
import csv


def cargar_paises():
    paises = []

    try:
        with open("paises.csv", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for pais in lector:
                paises.append(pais)

    except FileNotFoundError:
        print("No se encontro el archivo paises.csv")

    return paises


def guardar_paises(lista_paises):

    with open(
        "paises.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo:

        campos = [
            "nombre",
            "poblacion",
            "superficie",
            "continente"
        ]

        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos
        )

        escritor.writeheader()

        for pais in lista_paises:
            escritor.writerow(pais)


def mostrar_paises(lista_paises):

    print("\n===== LISTA DE PAISES =====")

    for pais in lista_paises:

        print(
            f"{pais['nombre']} - "
            f"Poblacion: {pais['poblacion']} - "
            f"Superficie: {pais['superficie']} - "
            f"Continente: {pais['continente']}"
        )


def agregar_pais(lista_paises):

    nombre = input("Nombre del pais: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacio")
        return

    poblacion = input("Poblacion: ").strip()
    superficie = input("Superficie: ").strip()
    continente = input("Continente: ").strip()

    if poblacion == "" or superficie == "" or continente == "":
        print("No se permiten campos vacios")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    lista_paises.append(nuevo_pais)

    guardar_paises(lista_paises)

    print("Pais agregado correctamente")


def actualizar_pais(lista_paises):

    nombre_buscado = input(
        "Ingrese el nombre del pais a actualizar: "
    ).strip()

    for pais in lista_paises:

        if pais["nombre"].lower() == nombre_buscado.lower():

            pais["poblacion"] = input(
                "Nueva poblacion: "
            ).strip()

            pais["superficie"] = input(
                "Nueva superficie: "
            ).strip()

            guardar_paises(lista_paises)

            print("Pais actualizado correctamente")
            return

    print("Pais no encontrado")


def buscar_pais(lista_paises):

    texto = input(
        "Ingrese el nombre del pais a buscar: "
    ).strip().lower()

    encontrado = False

    for pais in lista_paises:

        if texto in pais["nombre"].lower():

            print(
                f"\n{pais['nombre']} - "
                f"Poblacion: {pais['poblacion']} - "
                f"Superficie: {pais['superficie']} - "
                f"Continente: {pais['continente']}"
            )

            encontrado = True

    if not encontrado:
        print("No se encontraron paises")


def filtrar_continente(lista_paises):

    continente = input(
        "Ingrese el continente: "
    ).strip().lower()

    encontrados = 0

    for pais in lista_paises:

        if pais["continente"].lower() == continente:

            print(
                f"{pais['nombre']} - "
                f"Poblacion: {pais['poblacion']} - "
                f"Superficie: {pais['superficie']} - "
                f"Continente: {pais['continente']}"
            )

            encontrados += 1

    if encontrados == 0:
        print("No se encontraron paises")


def filtrar_poblacion(lista_paises):

    minimo = int(input("Poblacion minima: "))
    maximo = int(input("Poblacion maxima: "))

    encontrados = 0

    for pais in lista_paises:

        poblacion = int(pais["poblacion"])

        if minimo <= poblacion <= maximo:

            print(
                f"{pais['nombre']} - "
                f"Poblacion: {pais['poblacion']} - "
                f"Superficie: {pais['superficie']} - "
                f"Continente: {pais['continente']}"
            )

            encontrados += 1

    if encontrados == 0:
        print("No se encontraron paises")


def filtrar_superficie(lista_paises):

    minimo = int(input("Superficie minima: "))
    maximo = int(input("Superficie maxima: "))

    encontrados = 0

    for pais in lista_paises:

        superficie = int(pais["superficie"])

        if minimo <= superficie <= maximo:

            print(
                f"{pais['nombre']} - "
                f"Poblacion: {pais['poblacion']} - "
                f"Superficie: {pais['superficie']} - "
                f"Continente: {pais['continente']}"
            )

            encontrados += 1

    if encontrados == 0:
        print("No se encontraron paises")


def ordenar_nombre(lista_paises):

    ordenados = sorted(
        lista_paises,
        key=lambda pais: pais["nombre"]
    )

    mostrar_paises(ordenados)


def ordenar_poblacion(lista_paises):

    ordenados = sorted(
        lista_paises,
        key=lambda pais: int(pais["poblacion"])
    )

    mostrar_paises(ordenados)


def ordenar_superficie(lista_paises):

    ordenados = sorted(
        lista_paises,
        key=lambda pais: int(pais["superficie"])
    )

    mostrar_paises(ordenados)


def mostrar_estadisticas(lista_paises):

    mayor = max(
        lista_paises,
        key=lambda pais: int(pais["poblacion"])
    )

    menor = min(
        lista_paises,
        key=lambda pais: int(pais["poblacion"])
    )

    promedio_poblacion = sum(
        int(pais["poblacion"])
        for pais in lista_paises
    ) / len(lista_paises)

    promedio_superficie = sum(
        int(pais["superficie"])
        for pais in lista_paises
    ) / len(lista_paises)

    continentes = {}

    for pais in lista_paises:

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\n===== ESTADISTICAS =====")

    print(f"Pais con mayor poblacion: {mayor['nombre']}")
    print(f"Pais con menor poblacion: {menor['nombre']}")
    print(f"Promedio de poblacion: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")

    print("\nCantidad de paises por continente:")

    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")


lista_paises = cargar_paises()

while True:

    print("\n===== MENU PRINCIPAL =====")
    print("1. Mostrar paises")
    print("2. Agregar pais")
    print("3. Actualizar pais")
    print("4. Buscar pais")
    print("5. Filtrar por continente")
    print("6. Filtrar por poblacion")
    print("7. Filtrar por superficie")
    print("8. Ordenar por nombre")
    print("9. Ordenar por poblacion")
    print("10. Ordenar por superficie")
    print("11. Estadisticas")
    print("12. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        mostrar_paises(lista_paises)

    elif opcion == "2":
        agregar_pais(lista_paises)

    elif opcion == "3":
        actualizar_pais(lista_paises)

    elif opcion == "4":
        buscar_pais(lista_paises)

    elif opcion == "5":
        filtrar_continente(lista_paises)

    elif opcion == "6":
        filtrar_poblacion(lista_paises)

    elif opcion == "7":
        filtrar_superficie(lista_paises)

    elif opcion == "8":
        ordenar_nombre(lista_paises)

    elif opcion == "9":
        ordenar_poblacion(lista_paises)

    elif opcion == "10":
        ordenar_superficie(lista_paises)

    elif opcion == "11":
        mostrar_estadisticas(lista_paises)

    elif opcion == "12":
        print("Programa finalizado")
        break

    else:
=======
import csv


def cargar_paises():
    paises = []

    try:
        with open("paises.csv", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for pais in lector:
                paises.append(pais)

    except FileNotFoundError:
        print("No se encontro el archivo paises.csv")

    return paises


def guardar_paises(lista_paises):

    with open(
        "paises.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo:

        campos = [
            "nombre",
            "poblacion",
            "superficie",
            "continente"
        ]

        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos
        )

        escritor.writeheader()

        for pais in lista_paises:
            escritor.writerow(pais)


def mostrar_paises(lista_paises):

    print("\n===== LISTA DE PAISES =====")

    for pais in lista_paises:

        print(
            f"{pais['nombre']} - "
            f"Poblacion: {pais['poblacion']} - "
            f"Superficie: {pais['superficie']} - "
            f"Continente: {pais['continente']}"
        )


def agregar_pais(lista_paises):

    nombre = input("Nombre del pais: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacio")
        return

    poblacion = input("Poblacion: ").strip()
    superficie = input("Superficie: ").strip()
    continente = input("Continente: ").strip()

    if poblacion == "" or superficie == "" or continente == "":
        print("No se permiten campos vacios")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    lista_paises.append(nuevo_pais)

    guardar_paises(lista_paises)

    print("Pais agregado correctamente")


def actualizar_pais(lista_paises):

    nombre_buscado = input(
        "Ingrese el nombre del pais a actualizar: "
    ).strip()

    for pais in lista_paises:

        if pais["nombre"].lower() == nombre_buscado.lower():

            pais["poblacion"] = input(
                "Nueva poblacion: "
            ).strip()

            pais["superficie"] = input(
                "Nueva superficie: "
            ).strip()

            guardar_paises(lista_paises)

            print("Pais actualizado correctamente")
            return

    print("Pais no encontrado")


def buscar_pais(lista_paises):

    texto = input(
        "Ingrese el nombre del pais a buscar: "
    ).strip().lower()

    encontrado = False

    for pais in lista_paises:

        if texto in pais["nombre"].lower():

            print(
                f"\n{pais['nombre']} - "
                f"Poblacion: {pais['poblacion']} - "
                f"Superficie: {pais['superficie']} - "
                f"Continente: {pais['continente']}"
            )

            encontrado = True

    if not encontrado:
        print("No se encontraron paises")


def filtrar_continente(lista_paises):

    continente = input(
        "Ingrese el continente: "
    ).strip().lower()

    encontrados = 0

    for pais in lista_paises:

        if pais["continente"].lower() == continente:

            print(
                f"{pais['nombre']} - "
                f"Poblacion: {pais['poblacion']} - "
                f"Superficie: {pais['superficie']} - "
                f"Continente: {pais['continente']}"
            )

            encontrados += 1

    if encontrados == 0:
        print("No se encontraron paises")


def filtrar_poblacion(lista_paises):

    minimo = int(input("Poblacion minima: "))
    maximo = int(input("Poblacion maxima: "))

    encontrados = 0

    for pais in lista_paises:

        poblacion = int(pais["poblacion"])

        if minimo <= poblacion <= maximo:

            print(
                f"{pais['nombre']} - "
                f"Poblacion: {pais['poblacion']} - "
                f"Superficie: {pais['superficie']} - "
                f"Continente: {pais['continente']}"
            )

            encontrados += 1

    if encontrados == 0:
        print("No se encontraron paises")


def filtrar_superficie(lista_paises):

    minimo = int(input("Superficie minima: "))
    maximo = int(input("Superficie maxima: "))

    encontrados = 0

    for pais in lista_paises:

        superficie = int(pais["superficie"])

        if minimo <= superficie <= maximo:

            print(
                f"{pais['nombre']} - "
                f"Poblacion: {pais['poblacion']} - "
                f"Superficie: {pais['superficie']} - "
                f"Continente: {pais['continente']}"
            )

            encontrados += 1

    if encontrados == 0:
        print("No se encontraron paises")


def ordenar_nombre(lista_paises):

    ordenados = sorted(
        lista_paises,
        key=lambda pais: pais["nombre"]
    )

    mostrar_paises(ordenados)


def ordenar_poblacion(lista_paises):

    ordenados = sorted(
        lista_paises,
        key=lambda pais: int(pais["poblacion"])
    )

    mostrar_paises(ordenados)


def ordenar_superficie(lista_paises):

    ordenados = sorted(
        lista_paises,
        key=lambda pais: int(pais["superficie"])
    )

    mostrar_paises(ordenados)


def mostrar_estadisticas(lista_paises):

    mayor = max(
        lista_paises,
        key=lambda pais: int(pais["poblacion"])
    )

    menor = min(
        lista_paises,
        key=lambda pais: int(pais["poblacion"])
    )

    promedio_poblacion = sum(
        int(pais["poblacion"])
        for pais in lista_paises
    ) / len(lista_paises)

    promedio_superficie = sum(
        int(pais["superficie"])
        for pais in lista_paises
    ) / len(lista_paises)

    continentes = {}

    for pais in lista_paises:

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\n===== ESTADISTICAS =====")

    print(f"Pais con mayor poblacion: {mayor['nombre']}")
    print(f"Pais con menor poblacion: {menor['nombre']}")
    print(f"Promedio de poblacion: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")

    print("\nCantidad de paises por continente:")

    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")


lista_paises = cargar_paises()

while True:

    print("\n===== MENU PRINCIPAL =====")
    print("1. Mostrar paises")
    print("2. Agregar pais")
    print("3. Actualizar pais")
    print("4. Buscar pais")
    print("5. Filtrar por continente")
    print("6. Filtrar por poblacion")
    print("7. Filtrar por superficie")
    print("8. Ordenar por nombre")
    print("9. Ordenar por poblacion")
    print("10. Ordenar por superficie")
    print("11. Estadisticas")
    print("12. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        mostrar_paises(lista_paises)

    elif opcion == "2":
        agregar_pais(lista_paises)

    elif opcion == "3":
        actualizar_pais(lista_paises)

    elif opcion == "4":
        buscar_pais(lista_paises)

    elif opcion == "5":
        filtrar_continente(lista_paises)

    elif opcion == "6":
        filtrar_poblacion(lista_paises)

    elif opcion == "7":
        filtrar_superficie(lista_paises)

    elif opcion == "8":
        ordenar_nombre(lista_paises)

    elif opcion == "9":
        ordenar_poblacion(lista_paises)

    elif opcion == "10":
        ordenar_superficie(lista_paises)

    elif opcion == "11":
        mostrar_estadisticas(lista_paises)

    elif opcion == "12":
        print("Programa finalizado")
        break

    else:
>>>>>>> f7141f76bec230bcfcfeb17590d9365b3f91b1fe
        print("Opcion invalida")